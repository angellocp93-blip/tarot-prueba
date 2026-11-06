/* ==========================================================================
   78 MAPAS VISUALES DEL TAROT - SISTEMA Y LOGICA DE LA PLATAFORMA
   Optimizado para Móviles (Android / iPhone) & Generador de PDF
   ========================================================================== */

(function () {
  'use strict';

  // State Management with LocalStorage persistence
  const STORAGE_KEY = 'tarot_platform_state_v1';
  let appState = {
    selectedCardId: 'el-loco',
    mapViewMode: 'mindmap', // 'mindmap' | 'sheet' | 'guide'
    activeFilter: 'all',
    activeSpreadId: 'pasado-presente-futuro',
    allowReversals: true,
    masteredCards: [],
    difficultCards: [],
    quizIndex: 0,
    quizScore: 0,
    flashcardIndex: 0,
    flashcardFlipped: false
  };

  let activeAudioPlayer = null;

  // Load persisted state
  try {
    const saved = localStorage.getItem(STORAGE_KEY);
    if (saved) {
      const parsed = JSON.parse(saved);
      appState = { ...appState, ...parsed };
    }
  } catch (e) {
    console.error('Error loading state from localStorage:', e);
  }

  function saveState() {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(appState));
      updateProgressDisplay();
    } catch (e) {
      console.error('Error saving state:', e);
    }
  }

  // Audio synthesis for magical interactions (No external audio files required!)
  const audioCtx = (window.AudioContext || window.webkitAudioContext) ? new (window.AudioContext || window.webkitAudioContext)() : null;
  function playMysticChime(freq = 528) {
    if (!audioCtx) return;
    try {
      if (audioCtx.state === 'suspended') audioCtx.resume();
      const osc = audioCtx.createOscillator();
      const gain = audioCtx.createGain();
      osc.type = 'sine';
      osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
      gain.gain.setValueAtTime(0.08, audioCtx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 1.2);
      osc.connect(gain);
      gain.connect(audioCtx.destination);
      osc.start();
      osc.stop(audioCtx.currentTime + 1.2);
    } catch (e) {}
  }

  function playCardShuffleSound() {
    if (!audioCtx) return;
    try {
      if (audioCtx.state === 'suspended') audioCtx.resume();
      for (let i = 0; i < 5; i++) {
        setTimeout(() => {
          const osc = audioCtx.createOscillator();
          const gain = audioCtx.createGain();
          osc.type = 'triangle';
          osc.frequency.setValueAtTime(200 + Math.random() * 300, audioCtx.currentTime);
          gain.gain.setValueAtTime(0.04, audioCtx.currentTime);
          gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.15);
          osc.connect(gain);
          gain.connect(audioCtx.destination);
          osc.start();
          osc.stop(audioCtx.currentTime + 0.15);
        }, i * 60);
      }
    } catch (e) {}
  }

  // Toast Notification helper
  function showToast(icon, message, duration = 3200) {
    const toast = document.getElementById('toast-notification');
    if (!toast) return;
    document.getElementById('toast-icon').textContent = icon;
    document.getElementById('toast-message').textContent = message;
    toast.style.display = 'flex';
    clearTimeout(window._toastTimeout);
    window._toastTimeout = setTimeout(() => {
      toast.style.display = 'none';
    }, duration);
  }

  // DOM Elements cache
  const navTabsContainer = document.getElementById('nav-tabs-container');
  const mobileBottomNav = document.getElementById('mobile-bottom-nav');
  const tabPanes = document.querySelectorAll('.tab-pane');
  const cardsScrollList = document.getElementById('cards-scroll-list');
  const cardViewContainer = document.getElementById('card-view-container');
  const mapFilterPills = document.getElementById('map-filter-pills');
  const globalSearchInput = document.getElementById('global-search-input');
  const headerProgressText = document.getElementById('header-progress-text');
  const headerProgressPill = document.getElementById('header-progress-pill');

  // Mobile Navigator & Drawer
  const mNavCardName = document.getElementById('m-nav-card-name');
  const btnPrevCard = document.getElementById('btn-prev-card');
  const btnNextCard = document.getElementById('btn-next-card');
  const btnOpenCardDrawer = document.getElementById('btn-open-card-drawer');
  const cardDrawerOverlay = document.getElementById('card-drawer-overlay');
  const drawerCloseBtn = document.getElementById('drawer-close-btn');
  const drawerSearchInput = document.getElementById('drawer-search-input');
  const drawerFilterPills = document.getElementById('drawer-filter-pills');
  const drawerCardsGrid = document.getElementById('drawer-cards-grid');
  let drawerActiveFilter = 'all';

  // Map Controls
  const btnStarCard = document.getElementById('btn-star-card');
  const btnCheckCard = document.getElementById('btn-check-card');
  const btnDownloadPdf = document.getElementById('btn-download-pdf');
  const btnPrintMap = document.getElementById('btn-print-map');

  // Spreads Elements
  const spreadsSelectorBar = document.getElementById('spreads-selector-bar');
  const activeSpreadTitle = document.getElementById('active-spread-title');
  const matSlotsArea = document.getElementById('mat-slots-area');
  const btnDealSpread = document.getElementById('btn-deal-spread');
  const btnDownloadSpreadPdf = document.getElementById('btn-download-spread-pdf');
  const readingPanelContent = document.getElementById('reading-panel-content');
  const allowReversalsToggle = document.getElementById('allow-reversals-toggle');

  // Combinations Elements
  const comboSelectA = document.getElementById('combo-select-a');
  const comboSelectB = document.getElementById('combo-select-b');
  const comboResultDisplay = document.getElementById('combo-result-display');
  const iconicCombosGrid = document.getElementById('iconic-combos-grid');

  // Printable Deck Elements
  const deckGalleryGrid = document.getElementById('deck-gallery-grid');
  const btnPrintDeck = document.getElementById('btn-print-deck');

  // Inverted Cards Elements
  const invertedDictionaryGrid = document.getElementById('inverted-dictionary-grid');

  // Practice App Elements
  const practiceCardBtns = document.querySelectorAll('.practice-card-btn');
  const practiceSubpanes = {
    quiz: document.getElementById('practice-quiz-pane'),
    flashcards: document.getElementById('practice-flashcards-pane'),
    progress: document.getElementById('practice-progress-pane')
  };
  const quizContainer = document.getElementById('quiz-container');
  const flashcardStage = document.getElementById('flashcard-stage');
  const progressSummaryGrid = document.getElementById('progress-summary-grid');

  // Helper functions to get cards
  function getCardById(id) {
    return TAROT_DB.cards.find(c => c.id === id) || TAROT_DB.cards[0];
  }

  // ==========================================================================
  // NAVIGATION & TAB SWITCHING (DESKTOP & MOBILE)
  // ==========================================================================
  function switchTab(targetTabId) {
    // Desktop tabs
    document.querySelectorAll('.nav-btn').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.tab === targetTabId);
    });

    // Mobile bottom navigation bar
    document.querySelectorAll('.mobile-nav-btn').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.tab === targetTabId);
    });

    tabPanes.forEach(pane => {
      pane.classList.toggle('active', pane.id === targetTabId);
    });

    window.scrollTo({ top: 0, behavior: 'smooth' });
    playMysticChime(440);
  }

  navTabsContainer.addEventListener('click', (e) => {
    const btn = e.target.closest('.nav-btn');
    if (!btn) return;
    switchTab(btn.dataset.tab);
  });

  if (mobileBottomNav) {
    mobileBottomNav.addEventListener('click', (e) => {
      const btn = e.target.closest('.mobile-nav-btn');
      if (!btn) return;
      switchTab(btn.dataset.tab);
    });
  }

  document.getElementById('brand-home-btn').addEventListener('click', () => {
    switchTab('tab-mapas');
  });

  headerProgressPill.addEventListener('click', () => {
    switchTab('tab-practica');
    switchPracticeSubmode('progress');
  });

  // ==========================================================================
  // TAB 1: 78 MAPAS VISUALES - SIDEBAR & MAP VIEWER
  // ==========================================================================
  function renderCardsSidebar() {
    cardsScrollList.innerHTML = '';
    const filter = appState.activeFilter;

    let filteredCards = TAROT_DB.cards.filter(c => {
      if (filter === 'all') return true;
      if (filter === 'major') return c.type === 'Arcano Mayor';
      if (filter === 'bastos') return c.suit === 'Bastos';
      if (filter === 'copas') return c.suit === 'Copas';
      if (filter === 'espadas') return c.suit === 'Espadas';
      if (filter === 'oros') return c.suit === 'Oros';
      if (filter === 'difficult') return appState.difficultCards.includes(c.id);
      if (filter === 'mastered') return appState.masteredCards.includes(c.id);
      return true;
    });

    // Check search query
    const query = globalSearchInput.value.trim().toLowerCase();
    if (query) {
      filteredCards = filteredCards.filter(c => {
        return c.name.toLowerCase().includes(query) ||
               c.essence.toLowerCase().includes(query) ||
               c.keywords.some(k => k.toLowerCase().includes(query)) ||
               c.symbols.some(s => s.name.toLowerCase().includes(query) || s.desc.toLowerCase().includes(query));
      });
    }

    if (filteredCards.length === 0) {
      cardsScrollList.innerHTML = `<div style="padding: 1.5rem; text-align: center; color: var(--text-muted); font-size: 0.85rem;">No se encontraron cartas con este filtro.</div>`;
      return;
    }

    filteredCards.forEach(card => {
      const isSelected = card.id === appState.selectedCardId;
      const isMastered = appState.masteredCards.includes(card.id);
      const isDifficult = appState.difficultCards.includes(card.id);

      const item = document.createElement('div');
      item.className = `card-item ${isSelected ? 'selected' : ''}`;
      item.dataset.id = card.id;

      item.innerHTML = `
        <img class="card-item-thumb" src="${card.img}" alt="${card.name}" loading="lazy">
        <div class="card-item-info">
          <div class="card-item-name">${card.name}</div>
          <div class="card-item-type">${card.type === 'Arcano Mayor' ? `Arcano Mayor ${card.roman}` : `${card.suit} · ${card.element}`}</div>
        </div>
        <div class="card-item-badges">
          ${isMastered ? '<span title="Dominada">✅</span>' : ''}
          ${isDifficult ? '<span title="Repasar">⭐</span>' : ''}
        </div>
      `;

      item.addEventListener('click', () => {
        selectCard(card.id);
      });

      cardsScrollList.appendChild(item);
    });
  }

  function selectCard(cardId) {
    appState.selectedCardId = cardId;
    saveState();
    renderCardsSidebar();
    renderActiveCardView();
    updateMapButtonsState();
    updateMobileNavigator();
    playMysticChime(528);
  }

  mapFilterPills.addEventListener('click', (e) => {
    const btn = e.target.closest('.filter-btn');
    if (!btn) return;
    mapFilterPills.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    appState.activeFilter = btn.dataset.filter;
    renderCardsSidebar();
  });

  // Global search input
  globalSearchInput.addEventListener('input', () => {
    renderCardsSidebar();
  });

  // View mode switcher (mindmap / sheet / guide)
  document.querySelectorAll('.view-mode-selector .mode-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.view-mode-selector .mode-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      appState.mapViewMode = btn.dataset.mode;
      renderActiveCardView();
    });
  });

  function updateMapButtonsState() {
    const cardId = appState.selectedCardId;
    const isMastered = appState.masteredCards.includes(cardId);
    const isDifficult = appState.difficultCards.includes(cardId);

    btnCheckCard.classList.toggle('active-check', isMastered);
    btnCheckCard.innerHTML = isMastered ? '<span>✅</span> Dominada' : '<span>✔️</span> Marcar Dominada';

    btnStarCard.classList.toggle('active-star', isDifficult);
    btnStarCard.innerHTML = isDifficult ? '<span>⭐</span> En Repaso' : '<span>⭐</span> Me cuesta';
  }

  btnCheckCard.addEventListener('click', () => {
    const id = appState.selectedCardId;
    if (appState.masteredCards.includes(id)) {
      appState.masteredCards = appState.masteredCards.filter(c => c !== id);
      showToast('ℹ️', 'Carta desmarcada de dominadas');
    } else {
      appState.masteredCards.push(id);
      appState.difficultCards = appState.difficultCards.filter(c => c !== id);
      showToast('✅', '¡Carta marcada como dominada!');
      playMysticChime(660);
    }
    saveState();
    updateMapButtonsState();
    renderCardsSidebar();
  });

  btnStarCard.addEventListener('click', () => {
    const id = appState.selectedCardId;
    if (appState.difficultCards.includes(id)) {
      appState.difficultCards = appState.difficultCards.filter(c => c !== id);
      showToast('ℹ️', 'Carta removida de repaso');
    } else {
      appState.difficultCards.push(id);
      showToast('⭐', 'Carta agregada a "Lo que más te cuesta"');
      playMysticChime(380);
    }
    saveState();
    updateMapButtonsState();
    renderCardsSidebar();
  });

  btnPrintMap.addEventListener('click', () => {
    const prevMode = appState.mapViewMode;
    appState.mapViewMode = 'sheet';
    renderActiveCardView();
    window.print();
    setTimeout(() => {
      appState.mapViewMode = prevMode;
      renderActiveCardView();
    }, 500);
  });

  // Preload image as Base64 to guarantee html2canvas never fails or renders blank
  function getBase64Image(url) {
    return new Promise((resolve) => {
      const img = new Image();
      img.crossOrigin = 'anonymous';
      img.onload = () => {
        try {
          const canvas = document.createElement('canvas');
          canvas.width = img.naturalWidth || img.width || 300;
          canvas.height = img.naturalHeight || img.height || 500;
          const ctx = canvas.getContext('2d');
          ctx.drawImage(img, 0, 0);
          const dataURL = canvas.toDataURL('image/png');
          resolve(dataURL);
        } catch (e) {
          resolve(url);
        }
      };
      img.onerror = () => resolve(url);
      img.src = url;
    });
  }

  // ==========================================================================
  // DESCARGA DIRECTA EN PDF CON HTML2PDF (CAPTURA EN PANTALLA FIABLE)
  // ==========================================================================
  async function generateCardPdf(card) {
    showToast('⏳', `Generando PDF de ${card.name}...`, 8000);

    // Preload image to base64 so html2canvas renders image instantly without blank spots
    const base64Img = await getBase64Image(card.img);

    // Create rendering overlay in-viewport so html2canvas doesn't calculate negative/empty coords
    const overlay = document.createElement('div');
    overlay.id = 'pdf-render-overlay';
    overlay.style.cssText = `
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: rgba(10, 8, 22, 0.95);
      backdrop-filter: blur(8px);
      z-index: 999999;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: flex-start;
      overflow-y: auto;
      padding: 30px 15px;
      box-sizing: border-box;
    `;

    const statusEl = document.createElement('div');
    statusEl.style.cssText = `
      color: #fce99f;
      font-family: 'Cinzel', Georgia, serif;
      font-size: 1.1rem;
      font-weight: 700;
      margin-bottom: 20px;
      display: flex;
      align-items: center;
      gap: 12px;
    `;
    statusEl.innerHTML = `<div class="pdf-spinner"></div> Generando archivo PDF de ${card.name}...`;
    overlay.appendChild(statusEl);

    const targetBox = document.createElement('div');
    targetBox.id = 'pdf-render-target';
    targetBox.style.cssText = `
      width: 1020px;
      max-width: 1020px;
      background: #ffffff !important;
      color: #1a162b !important;
      border-radius: 8px;
      box-shadow: 0 10px 40px rgba(0, 0, 0, 0.8);
      overflow: hidden;
      box-sizing: border-box;
    `;
    targetBox.innerHTML = getSheetViewHtml(card, base64Img);
    overlay.appendChild(targetBox);

    document.body.appendChild(overlay);

    // Wait for DOM reflow
    await new Promise(r => setTimeout(r, 400));

    const safeFilename = `Mapa_Tarot_${card.name.replace(/\s+/g, '_')}.pdf`;

    if (window.html2pdf) {
      const opt = {
        margin: [6, 6, 6, 6],
        filename: safeFilename,
        image: { type: 'jpeg', quality: 0.98 },
        html2canvas: {
          scale: 2,
          useCORS: true,
          logging: false,
          scrollY: 0,
          scrollX: 0
        },
        jsPDF: { unit: 'mm', format: 'a4', orientation: 'landscape' }
      };

      try {
        await window.html2pdf().set(opt).from(targetBox).save();
        showToast('📥', `¡PDF de ${card.name} descargado!`);
        playMysticChime(660);
      } catch (err) {
        console.error('html2pdf error:', err);
        showToast('⚠️', 'Abriendo visor para Guardar como PDF...');
        window.print();
      } finally {
        if (document.body.contains(overlay)) {
          document.body.removeChild(overlay);
        }
      }
    } else {
      if (document.body.contains(overlay)) {
        document.body.removeChild(overlay);
      }
      window.print();
    }
  }

  if (btnDownloadPdf) {
    btnDownloadPdf.addEventListener('click', () => {
      const card = getCardById(appState.selectedCardId);
      generateCardPdf(card);
    });
  }

  // ==========================================================================
  // MOBILE QUICK CARD NAVIGATOR & DRAWER (MODAL)
  // ==========================================================================
  function updateMobileNavigator() {
    if (!mNavCardName) return;
    const card = getCardById(appState.selectedCardId);
    mNavCardName.textContent = `${card.name} (${card.type === 'Arcano Mayor' ? card.roman : card.number})`;
  }

  if (btnPrevCard) {
    btnPrevCard.addEventListener('click', () => {
      const cards = TAROT_DB.cards;
      const idx = cards.findIndex(c => c.id === appState.selectedCardId);
      const prevIdx = (idx - 1 + cards.length) % cards.length;
      selectCard(cards[prevIdx].id);
    });
  }

  if (btnNextCard) {
    btnNextCard.addEventListener('click', () => {
      const cards = TAROT_DB.cards;
      const idx = cards.findIndex(c => c.id === appState.selectedCardId);
      const nextIdx = (idx + 1) % cards.length;
      selectCard(cards[nextIdx].id);
    });
  }

  function openCardDrawer() {
    renderDrawerCardsGrid();
    cardDrawerOverlay.style.display = 'flex';
    drawerSearchInput.value = '';
    playMysticChime(500);
  }

  function closeCardDrawer() {
    cardDrawerOverlay.style.display = 'none';
  }

  if (btnOpenCardDrawer) {
    btnOpenCardDrawer.addEventListener('click', openCardDrawer);
  }

  if (drawerCloseBtn) {
    drawerCloseBtn.addEventListener('click', closeCardDrawer);
  }

  cardDrawerOverlay.addEventListener('click', (e) => {
    if (e.target === cardDrawerOverlay) closeCardDrawer();
  });

  if (drawerFilterPills) {
    drawerFilterPills.addEventListener('click', (e) => {
      const btn = e.target.closest('.filter-btn');
      if (!btn) return;
      drawerFilterPills.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      drawerActiveFilter = btn.dataset.filter;
      renderDrawerCardsGrid();
    });
  }

  if (drawerSearchInput) {
    drawerSearchInput.addEventListener('input', () => {
      renderDrawerCardsGrid();
    });
  }

  function renderDrawerCardsGrid() {
    if (!drawerCardsGrid) return;
    drawerCardsGrid.innerHTML = '';
    const filter = drawerActiveFilter;

    let filtered = TAROT_DB.cards.filter(c => {
      if (filter === 'all') return true;
      if (filter === 'major') return c.type === 'Arcano Mayor';
      if (filter === 'bastos') return c.suit === 'Bastos';
      if (filter === 'copas') return c.suit === 'Copas';
      if (filter === 'espadas') return c.suit === 'Espadas';
      if (filter === 'oros') return c.suit === 'Oros';
      if (filter === 'difficult') return appState.difficultCards.includes(c.id);
      if (filter === 'mastered') return appState.masteredCards.includes(c.id);
      return true;
    });

    const query = drawerSearchInput ? drawerSearchInput.value.trim().toLowerCase() : '';
    if (query) {
      filtered = filtered.filter(c => 
        c.name.toLowerCase().includes(query) ||
        c.keywords.some(k => k.toLowerCase().includes(query))
      );
    }

    filtered.forEach(card => {
      const isSelected = card.id === appState.selectedCardId;
      const chip = document.createElement('div');
      chip.className = `drawer-card-chip ${isSelected ? 'selected' : ''}`;
      chip.innerHTML = `
        <img class="drawer-card-thumb" src="${card.img}" alt="${card.name}">
        <div class="drawer-card-info">
          <div class="drawer-card-name">${card.name}</div>
          <div class="drawer-card-type">${card.type === 'Arcano Mayor' ? card.roman : card.suit}</div>
        </div>
      `;

      chip.addEventListener('click', () => {
        selectCard(card.id);
        closeCardDrawer();
      });

      drawerCardsGrid.appendChild(chip);
    });
  }

  // Render the selected card according to active mode
  function renderActiveCardView() {
    if (activeAudioPlayer) {
      try {
        activeAudioPlayer.pause();
      } catch (e) {}
      activeAudioPlayer = null;
    }
    const card = getCardById(appState.selectedCardId);
    cardViewContainer.innerHTML = '';

    if (appState.mapViewMode === 'mindmap') {
      renderMindMapView(card);
    } else if (appState.mapViewMode === 'sheet') {
      renderSheetView(card);
    } else {
      renderGuideView(card);
    }
  }

  // VISTA 1: MAPA MENTAL VISUAL
  function renderMindMapView(card) {
    const wrapper = document.createElement('div');
    wrapper.className = 'mindmap-canvas';

    const symbolsHtml = card.symbols.map(s => `
      <div class="symbol-item">
        <b>👁️ ${s.name}</b>
        <p>${s.desc}</p>
      </div>
    `).join('');

    wrapper.innerHTML = `
      <!-- Core Center Card -->
      <div class="mindmap-center-wrapper">
        <div class="mindmap-core-card">
          <img class="core-card-img" src="${card.img}" alt="${card.name}">
          <div class="core-card-meta">
            <div class="core-card-badges">
              <span class="badge-tag tag-gold">${card.type} · ${card.number}</span>
              <span class="badge-tag tag-element">${card.element}</span>
            </div>
            <h2 class="core-card-title">${card.name}</h2>
            <div class="core-card-keywords">${card.keywords.join(' · ')}</div>
            <div class="core-card-essence">"${card.essence}"</div>
          </div>
        </div>
      </div>

      <!-- Radial Branches Grid -->
      <div class="mindmap-nodes-grid">
        <!-- Node 1: Símbolos Clave -->
        <div class="map-node">
          <div class="node-header">
            <span class="node-icon">👁️</span>
            <span class="node-title">Símbolos Visuales Clave</span>
          </div>
          <div class="symbols-list">
            ${symbolsHtml}
          </div>
        </div>

        <!-- Node 2: Lado Luz & Lado Sombra -->
        <div class="map-node">
          <div class="node-header">
            <span class="node-icon">⚖️</span>
            <span class="node-title">Polaridad: Luz y Sombra</span>
          </div>
          <div class="polarity-pill polarity-light">
            <div class="polarity-title">☀️ Lado Luz (Virtudes & Dones)</div>
            <p style="font-size: 0.86rem; color: var(--text-main);">${card.light_side}</p>
          </div>
          <div class="polarity-pill polarity-shadow">
            <div class="polarity-title">🌑 Lado Sombra (Bloqueos & Excesos)</div>
            <p style="font-size: 0.86rem; color: var(--text-main);">${card.shadow_side}</p>
          </div>
        </div>

        <!-- Node 3: Amor & Relaciones -->
        <div class="map-node">
          <div class="node-header">
            <span class="node-icon">💖</span>
            <span class="node-title">En el Amor & Relaciones</span>
          </div>
          <p class="node-content">${card.love}</p>
        </div>

        <!-- Node 4: Trabajo & Dinero -->
        <div class="map-node">
          <div class="node-header">
            <span class="node-icon">💼</span>
            <span class="node-title">En el Trabajo & Dinero</span>
          </div>
          <p class="node-content">${card.work}</p>
        </div>

        <!-- Node 5: Espiritualidad -->
        <div class="map-node">
          <div class="node-header">
            <span class="node-icon">✨</span>
            <span class="node-title">Espiritualidad & Evolución</span>
          </div>
          <p class="node-content">${card.spirituality}</p>
        </div>

        <!-- Node 6: Consejo & Pregunta -->
        <div class="map-node">
          <div class="node-header">
            <span class="node-icon">🧭</span>
            <span class="node-title">Consejo & Pregunta Reflexiva</span>
          </div>
          <p class="node-content" style="margin-bottom: 0.75rem;">
            <b>Acción Inmediata:</b> ${card.advice}
          </p>
          <div style="background: rgba(212, 175, 55, 0.12); padding: 0.65rem 0.85rem; border-radius: 6px; border-left: 2px solid var(--gold-primary); font-size: 0.86rem; color: var(--gold-light);">
            <b>Pregunta para ti:</b> "${card.reflection_question}"
          </div>
        </div>

        <!-- Node 7: Carta Invertida -->
        <div class="map-node" style="grid-column: 1 / -1; border-color: rgba(244, 63, 94, 0.4);">
          <div class="node-header">
            <span class="node-icon" style="color: #fb7185;">🔄</span>
            <span class="node-title" style="color: #fb7185;">Significado Invertido (Al Revés)</span>
          </div>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem;">
            <div>
              <b style="color: #fca5a5; font-size: 0.88rem; display: block; margin-bottom: 0.25rem;">Palabras clave al revés:</b>
              <p style="font-size: 0.86rem; color: var(--text-muted);">${card.reversed.keywords.join(' · ')}</p>
              <p style="font-size: 0.88rem; margin-top: 0.5rem;">${card.reversed.meaning}</p>
            </div>
            <div style="background: rgba(0, 0, 0, 0.25); padding: 0.75rem; border-radius: 6px; border-left: 3px solid #10b981;">
              <b style="color: #34d399; font-size: 0.88rem; display: block; margin-bottom: 0.25rem;">🌿 Cómo armonizar / desbloquear:</b>
              <p style="font-size: 0.86rem; color: var(--text-main);">${card.reversed.how_to_heal}</p>
            </div>
          </div>
        </div>
      </div>
    `;

    cardViewContainer.appendChild(wrapper);
  }

  // HTML Builder for Sheet view (Used in both Sheet mode and PDF generator)
  function getSheetViewHtml(card, customImgSrc = null) {
    const imgSrc = customImgSrc || card.img;
    const symbolsList = card.symbols.map(s => `
      <li><b>${s.name}:</b> ${s.desc}</li>
    `).join('');

    return `
      <div class="sheet-container" style="background: #ffffff; color: #1a162b; padding: 2rem; max-width: 100%;">
        <div class="sheet-header" style="border-bottom: 2px solid #d4af37; padding-bottom: 1.25rem; margin-bottom: 1.25rem;">
          <img class="sheet-card-img" src="${imgSrc}" alt="${card.name}" style="width: 120px; height: 200px; border-radius: 6px; object-fit: cover; border: 2px solid #d4af37;">
          <div class="sheet-title-box">
            <span style="font-size: 0.8rem; font-weight: 700; color: #786b99; text-transform: uppercase;">
              ${card.type} · ${card.number} · Elemento ${card.element}
            </span>
            <h2 style="font-family: 'Cinzel', Georgia, serif; font-size: 1.85rem; color: #120e24; margin: 0.2rem 0;">${card.name}</h2>
            <div class="sheet-keywords" style="font-size: 0.95rem; color: #936f10; font-weight: 700; margin-bottom: 0.5rem;">${card.keywords.join(' · ')}</div>
            <div class="sheet-essence" style="font-size: 0.92rem; background: #fbf8eb; padding: 0.65rem 0.85rem; border-radius: 6px; border-left: 4px solid #d4af37; color: #332d4a; line-height: 1.45;"><b>Esencia:</b> "${card.essence}"</div>
          </div>
          <div style="text-align: right; font-size: 0.75rem; color: #888;">
            <div style="font-weight: 700; color: #936f10;">78 Mapas Mentales del Tarot</div>
            <div>Ficha de Consulta Rápida A4</div>
          </div>
        </div>

        <div class="sheet-grid" style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.25rem;">
          <div class="sheet-box" style="background: #f9f9fb; border: 1px solid #e2e0ea; border-radius: 8px; padding: 0.9rem 1.1rem;">
            <h3 style="font-family: 'Cinzel', Georgia, serif; font-size: 1rem; color: #18132e; border-bottom: 1px solid #d4af37; padding-bottom: 0.35rem; margin-bottom: 0.6rem;">👁️ Símbolos Visuales Clave</h3>
            <ul style="padding-left: 1.15rem; display: flex; flex-direction: column; gap: 0.35rem; font-size: 0.85rem; color: #3b3552; line-height: 1.45;">
              ${symbolsList}
            </ul>
          </div>

          <div class="sheet-box" style="background: #f9f9fb; border: 1px solid #e2e0ea; border-radius: 8px; padding: 0.9rem 1.1rem;">
            <h3 style="font-family: 'Cinzel', Georgia, serif; font-size: 1rem; color: #18132e; border-bottom: 1px solid #d4af37; padding-bottom: 0.35rem; margin-bottom: 0.6rem;">⚖️ Lado Luz y Lado Sombra</h3>
            <div style="margin-bottom: 0.65rem;">
              <b style="color: #059669; font-size: 0.88rem;">☀️ Lado Luz:</b>
              <p style="font-size: 0.85rem; color: #3b3552; margin-top: 0.15rem;">${card.light_side}</p>
            </div>
            <div>
              <b style="color: #e11d48; font-size: 0.88rem;">🌑 Lado Sombra:</b>
              <p style="font-size: 0.85rem; color: #3b3552; margin-top: 0.15rem;">${card.shadow_side}</p>
            </div>
          </div>

          <div class="sheet-box" style="background: #f9f9fb; border: 1px solid #e2e0ea; border-radius: 8px; padding: 0.9rem 1.1rem;">
            <h3 style="font-family: 'Cinzel', Georgia, serif; font-size: 1rem; color: #18132e; border-bottom: 1px solid #d4af37; padding-bottom: 0.35rem; margin-bottom: 0.6rem;">💖 Amor y Trabajo</h3>
            <p style="font-size: 0.85rem; color: #3b3552; margin-bottom: 0.65rem;"><b>Amor:</b> ${card.love}</p>
            <p style="font-size: 0.85rem; color: #3b3552;"><b>Trabajo y Dinero:</b> ${card.work}</p>
          </div>

          <div class="sheet-box" style="background: #f9f9fb; border: 1px solid #e2e0ea; border-radius: 8px; padding: 0.9rem 1.1rem;">
            <h3 style="font-family: 'Cinzel', Georgia, serif; font-size: 1rem; color: #18132e; border-bottom: 1px solid #d4af37; padding-bottom: 0.35rem; margin-bottom: 0.6rem;">🧭 Consejo & Carta Invertida</h3>
            <div style="margin-bottom: 0.5rem; font-size: 0.85rem; color: #3b3552;">
              <b>Acción:</b> ${card.advice}
            </div>
            <div style="margin-bottom: 0.65rem; font-size: 0.84rem; color: #3b3552; font-style: italic;">
              <b>Pregunta:</b> "${card.reflection_question}"
            </div>
            <div style="background: #fdf2f4; border-left: 3px solid #e11d48; padding: 0.45rem 0.65rem; border-radius: 4px; font-size: 0.82rem; color: #be123c;">
              <b>🔄 Al salir invertida:</b> ${card.reversed.meaning}
            </div>
          </div>
        </div>
      </div>
    `;
  }

  // VISTA 2: FICHA DE ESTUDIO RESUMEN A4
  function renderSheetView(card) {
    const wrapper = document.createElement('div');
    wrapper.innerHTML = getSheetViewHtml(card);
    cardViewContainer.appendChild(wrapper);
  }

  // VISTA 3: ESTUDIO PROFUNDO & AUDIOLIBRO
  function renderGuideView(card) {
    const wrapper = document.createElement('div');
    wrapper.className = 'study-view-container';

    // Formatter for time mm:ss
    function formatTime(seconds) {
      if (isNaN(seconds)) return '0:00';
      const m = Math.floor(seconds / 60);
      const s = Math.floor(seconds % 60);
      return `${m}:${s < 10 ? '0' : ''}${s}`;
    }

    const symbolsHtml = (card.symbols || []).map(s => `
      <div class="study-symbol-item">
        <b>👁️ ${s.name}</b>
        <p>${s.desc}</p>
      </div>
    `).join('');

    const curiositiesHtml = (card.curiosities || []).map(c => `
      <li>${c}</li>
    `).join('');

    // Formatear párrafos del relato
    const storyText = card.inspired_story?.relato || '';
    const storyParas = storyText.split('\n').filter(p => p.trim().length > 0).map(p => `<p>${p.trim()}</p>`).join('');

    // Audio path
    const audioSrc = card.audio?.archivo || `assets/audio/${card.id}.mp3`;
    const audioTitle = card.audio?.titulo || `${card.name} - Audiolibro y Meditación Guiada`;
    const audioDuration = card.audio?.duracion_estimada || '4:00 min';

    wrapper.innerHTML = `
      <!-- HERO HEADER -->
      <div class="study-hero-card">
        <div class="study-card-img-wrap">
          <img src="${card.img}" class="study-card-img" alt="${card.name}">
        </div>
        <div class="study-hero-info">
          <div class="study-meta-badges">
            <span class="study-badge study-badge-type">${card.type} · ${card.number}</span>
            <span class="study-badge study-badge-element">⚡ ${card.element}</span>
            <span class="study-badge study-badge-astro">🪐 ${card.astrology}</span>
          </div>
          <h1 class="study-card-title">${card.name}</h1>
          <div class="study-keywords-row">
            ${(card.keywords || []).map(k => `<span class="study-kw-chip">${k}</span>`).join('')}
          </div>
          <div class="study-essence-box">
            <b>Esencia Primordial:</b> ${card.essence || card.fundamental_meaning}
          </div>
        </div>
      </div>

      <!-- REPRODUCTOR DE AUDIOLIBRO MÍSTICO -->
      <div class="mystic-audio-card">
        <div class="audio-card-header">
          <div class="audio-header-title">
            <span>🎧</span> ${audioTitle}
          </div>
          <span class="audio-header-pill">Duración aprox. ${audioDuration}</span>
        </div>

        <audio id="card-audio-element" preload="metadata">
          <source src="${audioSrc}" type="audio/mpeg">
          Tu navegador no soporta el reproductor de audio.
        </audio>

        <div class="audio-controls-row">
          <button class="audio-play-btn" id="audio-play-btn" title="Reproducir / Pausar">
            <span id="audio-play-icon">▶</span>
          </button>

          <div class="audio-scrubber-box">
            <div class="audio-time-row">
              <span id="audio-current-time">0:00</span>
              <span id="audio-total-duration">--:--</span>
            </div>
            <div class="audio-progress-bar" id="audio-progress-bar">
              <div class="audio-progress-fill" id="audio-progress-fill"></div>
            </div>
          </div>

          <button class="audio-speed-btn" id="audio-speed-btn" title="Velocidad de reproducción">1.0x</button>
          <button class="audio-vol-btn" id="audio-vol-btn" title="Silenciar / Activar sonido">🔊</button>
        </div>

        <div class="audio-status-banner" id="audio-status-banner">
          <span>ℹ️</span>
          <span>Coloca tu archivo <code>${audioSrc}</code> en tu repositorio para escuchar el audiolibro.</span>
        </div>
      </div>

      <!-- 1. HISTORIA Y ORIGEN SIMBÓLICO -->
      <div class="study-section">
        <h3 class="study-section-title">
          <span>📜</span> 1. Historia y Origen Simbólico
        </h3>
        <p class="study-prose">
          ${card.history || 'Evolución iconográfica e histórica desde las cortes medievales renacentistas hasta la baraja Rider-Waite-Smith.'}
        </p>
      </div>

      <!-- 2. SIGNIFICADO FUNDAMENTAL & POLARIDAD -->
      <div class="study-section">
        <h3 class="study-section-title">
          <span>🔮</span> 2. Significado Fundamental & Polaridad
        </h3>
        <p class="study-prose" style="margin-bottom: 1.25rem;">
          ${card.fundamental_meaning || card.meaning_upright}
        </p>

        <div class="polarity-grid">
          <div class="polarity-card light">
            <h4>☀️ Polaridad de Luz</h4>
            <p style="margin: 0; font-size: 0.9rem; line-height: 1.5;">${card.light_side}</p>
          </div>
          <div class="polarity-card shadow">
            <h4>🌑 Polaridad de Sombra</h4>
            <p style="margin: 0; font-size: 0.9rem; line-height: 1.5;">${card.shadow_side}</p>
          </div>
        </div>
      </div>

      <!-- SÍMBOLOS VISUALES CLAVE -->
      <div class="study-section">
        <h3 class="study-section-title">
          <span>👁️</span> Símbolos Visuales Clave
        </h3>
        <div class="study-symbols-grid">
          ${symbolsHtml}
        </div>
      </div>

      <!-- 3. LA CARTA EN POSICIÓN NORMAL -->
      <div class="study-section">
        <h3 class="study-section-title">
          <span>☀️</span> 3. La Carta en Posición Normal (Los 4 Planos)
        </h3>
        <p class="study-prose" style="margin-bottom: 1rem;">
          <b>Resumen al derecho:</b> ${card.normal_position?.resumen || card.meaning_upright}
        </p>

        <div class="vital-planes-grid">
          <div class="plane-card">
            <div class="plane-card-header">
              <span>💖</span> En el Amor & Relaciones
            </div>
            <p class="plane-card-text">${card.normal_position?.amor || card.love}</p>
          </div>

          <div class="plane-card">
            <div class="plane-card-header">
              <span>💼</span> En el Dinero & Trabajo
            </div>
            <p class="plane-card-text">${card.normal_position?.dinero_trabajo || card.work}</p>
          </div>

          <div class="plane-card">
            <div class="plane-card-header">
              <span>🌿</span> En la Salud & Vitalidad
            </div>
            <p class="plane-card-text">${card.normal_position?.salud || 'Vitalidad en equilibrio y alineamiento con la energía del arcano.'}</p>
          </div>

          <div class="plane-card">
            <div class="plane-card-header">
              <span>✨</span> En la Espiritualidad
            </div>
            <p class="plane-card-text">${card.normal_position?.espiritualidad || card.spirituality}</p>
          </div>
        </div>
      </div>

      <!-- 4. LA CARTA EN POSICIÓN INVERTIDA -->
      <div class="study-section">
        <h3 class="study-section-title" style="color: #fb7185;">
          <span>🔄</span> 4. La Carta en Posición Invertida (Bloqueos y Sanación)
        </h3>
        <div style="font-size: 0.85rem; color: #fca5a5; margin-bottom: 0.6rem;">
          <b>Palabras clave invertidas:</b> ${(card.reversed?.keywords || []).join(' · ')}
        </div>
        <p class="study-prose" style="margin-bottom: 1rem;">
          <b>Resumen invertido:</b> ${card.reversed_position?.resumen || card.reversed?.meaning}
        </p>

        <div class="vital-planes-grid reversed" style="margin-bottom: 1.25rem;">
          <div class="plane-card">
            <div class="plane-card-header">
              <span>💔</span> Desafío en el Amor
            </div>
            <p class="plane-card-text">${card.reversed_position?.amor || 'Bloqueos afectivos o desconexión emocional.'}</p>
          </div>

          <div class="plane-card">
            <div class="plane-card-header">
              <span>📉</span> Desafío en el Trabajo
            </div>
            <p class="plane-card-text">${card.reversed_position?.dinero_trabajo || 'Retrasos o dispersión de esfuerzos profesionales.'}</p>
          </div>

          <div class="plane-card">
            <div class="plane-card-header">
              <span>🩺</span> Desafío en la Salud
            </div>
            <p class="plane-card-text">${card.reversed_position?.salud || 'Fatiga acumulada o somatización de estrés.'}</p>
          </div>

          <div class="plane-card">
            <div class="plane-card-header">
              <span>🌪️</span> Desafío en el Espíritu
            </div>
            <p class="plane-card-text">${card.reversed_position?.espiritualidad || 'Desconexión momentánea de la guía interior.'}</p>
          </div>
        </div>

        <div class="heal-box">
          <b>🌟 Cómo armonizar o desbloquear esta energía:</b><br>
          ${card.reversed?.how_to_heal || card.reversed_position?.como_armonizar_desbloquear}
        </div>
      </div>

      <!-- 5. LO QUE LO HACE ÚNICO FRENTE A SUS SIMILARES -->
      <div class="study-section">
        <h3 class="study-section-title">
          <span>💎</span> 5. Lo que lo hace Único frente a sus Similares
        </h3>
        <div class="unique-box">
          ${card.unique_differentiator || 'Diferenciación arquetípica respecto a cartas afines en la baraja.'}
        </div>
      </div>

      <!-- 6. CURIOSIDADES DEL ARCANO -->
      <div class="study-section">
        <h3 class="study-section-title">
          <span>💡</span> 6. Curiosidades del Arcano
        </h3>
        <ul class="curiosities-list">
          ${curiositiesHtml}
        </ul>
      </div>

      <!-- CONSEJO DEL ARCANO & PREGUNTA REFLEXIVA -->
      <div class="study-section">
        <h3 class="study-section-title">
          <span>🎯</span> Consejo del Arcano & Pregunta Reflexiva
        </h3>
        <div class="advice-reflection-grid">
          <div class="advice-card">
            <h4>⚡ Acción Inmediata (Consejo)</h4>
            <p style="margin: 0; font-size: 0.92rem; line-height: 1.55;">${card.advice}</p>
          </div>
          <div class="reflection-card">
            <h4>❓ Pregunta para ti</h4>
            <p style="margin: 0; font-size: 0.92rem; line-height: 1.55;">${card.reflection_question}</p>
          </div>
        </div>
      </div>

      <!-- 7. UNA HISTORIA INSPIRADA -->
      <div class="parable-card">
        <h3 class="parable-title">
          📖 ${card.inspired_story?.titulo || 'La Parábola del Arcano'}
        </h3>
        <div class="parable-text">
          ${storyParas}
        </div>
      </div>
    `;

    cardViewContainer.appendChild(wrapper);

    // Audio Player Interactivity
    const audioEl = wrapper.querySelector('#card-audio-element');
    const playBtn = wrapper.querySelector('#audio-play-btn');
    const playIcon = wrapper.querySelector('#audio-play-icon');
    const progressBar = wrapper.querySelector('#audio-progress-bar');
    const progressFill = wrapper.querySelector('#audio-progress-fill');
    const currentTimeEl = wrapper.querySelector('#audio-current-time');
    const totalDurationEl = wrapper.querySelector('#audio-total-duration');
    const speedBtn = wrapper.querySelector('#audio-speed-btn');
    const volBtn = wrapper.querySelector('#audio-vol-btn');
    const statusBanner = wrapper.querySelector('#audio-status-banner');

    if (audioEl) {
      activeAudioPlayer = audioEl;

      audioEl.addEventListener('loadedmetadata', () => {
        totalDurationEl.textContent = formatTime(audioEl.duration);
        if (statusBanner) statusBanner.style.display = 'none';
      });

      audioEl.addEventListener('timeupdate', () => {
        if (!isNaN(audioEl.duration) && audioEl.duration > 0) {
          const pct = (audioEl.currentTime / audioEl.duration) * 100;
          progressFill.style.width = `${pct}%`;
          currentTimeEl.textContent = formatTime(audioEl.currentTime);
        }
      });

      audioEl.addEventListener('ended', () => {
        playBtn.classList.remove('is-playing');
        playIcon.textContent = '▶';
        progressFill.style.width = '0%';
        currentTimeEl.textContent = '0:00';
      });

      audioEl.addEventListener('error', () => {
        if (statusBanner) {
          statusBanner.style.display = 'flex';
          statusBanner.innerHTML = `<span>ℹ️</span> <span>Audiolibro listo en la plataforma: sube <code>${audioSrc}</code> para escucharlo aquí.</span>`;
        }
      });

      // Play/Pause Click
      playBtn.addEventListener('click', () => {
        if (audioEl.paused) {
          const playPromise = audioEl.play();
          if (playPromise !== undefined) {
            playPromise.then(() => {
              playBtn.classList.add('is-playing');
              playIcon.textContent = '⏸';
              if (statusBanner) statusBanner.style.display = 'none';
            }).catch(() => {
              // Audio file not yet added to repo
              if (statusBanner) {
                statusBanner.style.display = 'flex';
                statusBanner.innerHTML = `<span>🎧</span> <span>Audiolibro en espera: agrega el archivo <b>${audioSrc}</b> en GitHub para reproducir.</span>`;
              }
              showToast('🎧', `Audiolibro en espera: agrega ${audioSrc}`);
            });
          }
        } else {
          audioEl.pause();
          playBtn.classList.remove('is-playing');
          playIcon.textContent = '▶';
        }
      });

      // Seek in progress bar
      progressBar.addEventListener('click', (e) => {
        const rect = progressBar.getBoundingClientRect();
        const pos = (e.clientX - rect.left) / rect.width;
        if (!isNaN(audioEl.duration) && audioEl.duration > 0) {
          audioEl.currentTime = pos * audioEl.duration;
        }
      });

      // Speed button cycle
      const speeds = [1.0, 1.25, 1.5];
      let speedIdx = 0;
      speedBtn.addEventListener('click', () => {
        speedIdx = (speedIdx + 1) % speeds.length;
        const spd = speeds[speedIdx];
        audioEl.playbackRate = spd;
        speedBtn.textContent = `${spd}x`;
      });

      // Volume / Mute button
      volBtn.addEventListener('click', () => {
        audioEl.muted = !audioEl.muted;
        volBtn.textContent = audioEl.muted ? '🔇' : '🔊';
      });
    }
  }

  // ==========================================================================
  // TAB 2: BONO 1 - GUIA DE 12 TIRADAS & SIMULADOR EN VIVO
  // ==========================================================================
  let spreadDealtCards = []; // { card, isReversed, isFlipped, position }

  function renderSpreadsSelector() {
    spreadsSelectorBar.innerHTML = '';
    TAROT_DB.spreads.forEach(spread => {
      const chip = document.createElement('div');
      chip.className = `spread-chip ${spread.id === appState.activeSpreadId ? 'active' : ''}`;
      chip.dataset.id = spread.id;
      chip.innerHTML = `<span>🃏</span> ${spread.name} (${spread.card_count})`;

      chip.addEventListener('click', () => {
        selectSpread(spread.id);
      });

      spreadsSelectorBar.appendChild(chip);
    });
  }

  function selectSpread(spreadId) {
    appState.activeSpreadId = spreadId;
    saveState();
    renderSpreadsSelector();
    loadSpreadStage();
    playMysticChime(500);
  }

  function loadSpreadStage() {
    const spread = TAROT_DB.spreads.find(s => s.id === appState.activeSpreadId) || TAROT_DB.spreads[1];
    activeSpreadTitle.textContent = `${spread.name} (${spread.card_count} Cartas)`;

    // Reset mat slots
    matSlotsArea.innerHTML = '';
    spreadDealtCards = [];
    if (btnDownloadSpreadPdf) btnDownloadSpreadPdf.style.display = 'none';

    // Reset reading panel
    readingPanelContent.innerHTML = `
      <div class="reading-card-focus">
        <h4 style="color: var(--gold-light); margin-bottom: 0.35rem;">Objetivo de la Tirada</h4>
        <p class="reading-card-focus-text">${spread.description}</p>
        <div style="margin-top: 0.75rem; font-size: 0.82rem; color: var(--gold-light);">
          <b>Cuándo usar:</b> ${spread.when_to_use}
        </div>
        <div style="margin-top: 1rem; border-top: 1px dashed rgba(255,255,255,0.1); padding-top: 0.75rem; color: var(--text-muted); font-size: 0.84rem;">
          Presiona <b>"Barajar y Tirar Cartas"</b> para repartir el mazo.
        </div>
      </div>
    `;

    // Render empty card back placeholder slots
    spread.positions.forEach(pos => {
      const slot = document.createElement('div');
      slot.className = 'spread-card-slot';
      slot.dataset.pos = pos.pos;

      slot.innerHTML = `
        <div class="card-inner">
          <div class="card-back">
            <img src="assets/card_back.svg" alt="Dorso de Tarot">
          </div>
          <div class="card-front">
            <img src="assets/card_back.svg" alt="Frente">
          </div>
        </div>
        <div class="slot-pos-badge">${pos.pos}. ${pos.name}</div>
      `;

      matSlotsArea.appendChild(slot);
    });
  }

  // Shuffle & Deal Spreads
  btnDealSpread.addEventListener('click', () => {
    dealActiveSpread();
  });

  function dealActiveSpread() {
    playCardShuffleSound();
    const spread = TAROT_DB.spreads.find(s => s.id === appState.activeSpreadId);
    const allowReversals = allowReversalsToggle.checked;

    // Pick unique random cards from 78
    const shuffled = [...TAROT_DB.cards].sort(() => 0.5 - Math.random());
    const pickedCards = shuffled.slice(0, spread.card_count);

    spreadDealtCards = pickedCards.map((card, idx) => ({
      card: card,
      position: spread.positions[idx],
      isReversed: allowReversals ? Math.random() < 0.28 : false,
      isFlipped: false
    }));

    if (btnDownloadSpreadPdf) btnDownloadSpreadPdf.style.display = 'inline-flex';

    // Update slots in mat
    const slots = matSlotsArea.querySelectorAll('.spread-card-slot');
    slots.forEach((slot, idx) => {
      const cardData = spreadDealtCards[idx];
      const inner = slot.querySelector('.card-inner');
      const frontImg = slot.querySelector('.card-front img');

      // Reset flip
      inner.className = 'card-inner';
      frontImg.src = cardData.card.img;

      // Click to flip card
      slot.onclick = () => {
        flipSlotCard(idx, slot, inner, cardData);
      };
    });

    readingPanelContent.innerHTML = `
      <div class="reading-card-focus">
        <h4 style="color: #34d399; margin-bottom: 0.4rem;">✨ Mazo Barajado y Repartido</h4>
        <p class="reading-card-focus-text">
          Las ${spread.card_count} cartas han sido colocadas en el tapete. <b>Toca cada carta</b> para revelarla y leer su mensaje para esa posición.
        </p>
      </div>
    `;

    showToast('🃏', `Cartas repartidas: ${spread.name}`);
  }

  function flipSlotCard(index, slotEl, innerEl, cardData) {
    if (!cardData.isFlipped) {
      cardData.isFlipped = true;
      innerEl.classList.add('is-flipped');
      if (cardData.isReversed) {
        innerEl.classList.add('is-reversed');
      }
      playMysticChime(580 + index * 40);
    }

    // Highlight slot
    matSlotsArea.querySelectorAll('.spread-card-slot').forEach(s => s.classList.remove('active-reading'));
    slotEl.classList.add('active-reading');

    // Display position reading in panel
    displayPositionReading(cardData);
  }

  function displayPositionReading(cardData) {
    const card = cardData.card;
    const pos = cardData.position;
    const isRev = cardData.isReversed;

    readingPanelContent.innerHTML = `
      <div class="reading-card-focus">
        <div class="reading-card-focus-pos">
          <b>POSICIÓN ${pos.pos}: ${pos.name.toUpperCase()}</b>
          <div style="font-size: 0.78rem; color: var(--gold-light); margin-top: 0.15rem;">${pos.desc}</div>
        </div>

        <div style="display: flex; gap: 1rem; align-items: center; margin-bottom: 0.85rem;">
          <img src="${card.img}" style="width: 55px; height: 95px; border-radius: 4px; border: 1px solid var(--gold-primary); ${isRev ? 'transform: rotate(180deg);' : ''}">
          <div>
            <div class="reading-card-focus-title">${card.name} ${isRev ? '<span style="color: #fb7185; font-size: 0.8rem;">(Invertida 🔄)</span>' : '<span style="color: #34d399; font-size: 0.8rem;">(Al Derecho ☀️)</span>'}</div>
            <div style="font-size: 0.8rem; color: var(--text-muted);">${card.keywords.slice(0, 3).join(' · ')}</div>
          </div>
        </div>

        <div class="reading-card-focus-text">
          <b>Mensaje para esta posición:</b>
          <p style="margin-top: 0.35rem;">
            ${isRev ? card.reversed.meaning : card.meaning_upright}
          </p>
        </div>

        <div style="margin-top: 0.75rem; background: rgba(212, 175, 55, 0.1); padding: 0.6rem 0.75rem; border-radius: 6px; font-size: 0.82rem;">
          <b>Consejo del Arcano:</b> ${card.advice}
        </div>
      </div>
    `;

    // On mobile, scroll reading panel smoothly into view if offscreen
    if (window.innerWidth <= 768) {
      readingPanelContent.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
  }

  // Descargar Informe de Tirada en PDF
  if (btnDownloadSpreadPdf) {
    btnDownloadSpreadPdf.addEventListener('click', async () => {
      const spread = TAROT_DB.spreads.find(s => s.id === appState.activeSpreadId);
      if (!spreadDealtCards || spreadDealtCards.length === 0) return;

      showToast('⏳', `Generando informe de ${spread.name}...`, 8000);

      // Pre-cargar imágenes en base64 para evitar canvas en blanco
      const cardBase64List = await Promise.all(spreadDealtCards.map(async (c) => {
        try {
          const b64 = await getBase64Image(c.card.img);
          return { ...c, base64Img: b64 || c.card.img };
        } catch (e) {
          return { ...c, base64Img: c.card.img };
        }
      }));

      const overlay = document.createElement('div');
      overlay.id = 'pdf-render-overlay';
      overlay.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background: rgba(10, 8, 22, 0.95);
        backdrop-filter: blur(8px);
        z-index: 999999;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-start;
        overflow-y: auto;
        padding: 30px 15px;
        box-sizing: border-box;
      `;

      const statusEl = document.createElement('div');
      statusEl.style.cssText = `
        color: #fce99f;
        font-family: 'Cinzel', Georgia, serif;
        font-size: 1.1rem;
        font-weight: 700;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        gap: 12px;
      `;
      statusEl.innerHTML = `<div class="pdf-spinner"></div> Generando informe PDF de la lectura...`;
      overlay.appendChild(statusEl);

      const targetBox = document.createElement('div');
      targetBox.id = 'pdf-render-target';
      targetBox.style.cssText = `
        width: 820px;
        max-width: 820px;
        background: #ffffff !important;
        color: #1a162b !important;
        border-radius: 8px;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.8);
        overflow: hidden;
        box-sizing: border-box;
        padding: 30px;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      `;

      const positionsHtml = cardBase64List.map(c => `
        <div style="border-bottom: 1px solid #e2e8f0; padding: 14px 0; display: flex; gap: 16px; align-items: flex-start; page-break-inside: avoid;">
          <img src="${c.base64Img}" style="width: 65px; height: 110px; border: 1.5px solid #d4af37; border-radius: 5px; object-fit: cover; flex-shrink: 0; ${c.isReversed ? 'transform: rotate(180deg);' : ''}">
          <div style="flex: 1;">
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 3px;">
              <b style="color: #997510; font-size: 13px; text-transform: uppercase; letter-spacing: 0.5px;">Posición ${c.position.pos}: ${c.position.name}</b>
              <span style="font-size: 11px; padding: 2px 7px; border-radius: 4px; background: ${c.isReversed ? '#fee2e2; color: #991b1b;' : '#dcfce7; color: #166534;'} font-weight: 600;">
                ${c.isReversed ? 'Invertida 🔄' : 'Al Derecho ☀️'}
              </span>
            </div>
            <div style="font-size: 11px; color: #64748b; margin-bottom: 6px; font-style: italic;">${c.position.desc}</div>
            <h4 style="margin: 0 0 6px 0; color: #0f172a; font-size: 16px;">${c.card.name}</h4>
            <p style="font-size: 12.5px; line-height: 1.5; color: #334155; margin: 0 0 6px 0;">${c.isReversed ? c.card.reversed.meaning : c.card.meaning_upright}</p>
            <div style="font-size: 11.5px; color: #065f46; background: #ecfdf5; padding: 5px 9px; border-radius: 4px; border-left: 3px solid #10b981;"><b>Consejo:</b> ${c.card.advice}</div>
          </div>
        </div>
      `).join('');

      targetBox.innerHTML = `
        <div style="border-bottom: 3px solid #d4af37; padding-bottom: 14px; margin-bottom: 16px; display: flex; justify-content: space-between; align-items: flex-end;">
          <div>
            <div style="font-size: 11px; color: #d4af37; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px;">Santuario de Tarot · 78 Mapas Mentales</div>
            <h1 style="margin: 3px 0 0 0; color: #0f172a; font-size: 24px; font-family: Georgia, serif;">Informe: ${spread.name}</h1>
          </div>
          <div style="text-align: right; font-size: 11.5px; color: #64748b;">
            <div><b>Fecha:</b> ${new Date().toLocaleDateString('es-ES', { year: 'numeric', month: 'long', day: 'numeric' })}</div>
            <div>${spread.card_count} Arcanos Consultados</div>
          </div>
        </div>
        <div style="font-size: 12.5px; color: #475569; margin-bottom: 16px; background: #f8fafc; padding: 10px 14px; border-radius: 6px; border: 1px solid #e2e8f0;">
          <b>Propósito de la Tirada:</b> ${spread.desc}
        </div>
        <div>${positionsHtml}</div>
        <div style="margin-top: 20px; padding-top: 10px; border-top: 1px solid #e2e8f0; font-size: 10.5px; color: #94a3b8; text-align: center;">
          Generado automáticamente por la Plataforma Interactiva de 78 Mapas Mentales de Tarot.
        </div>
      `;

      overlay.appendChild(targetBox);
      document.body.appendChild(overlay);

      // Esperar renderizado y layout del DOM
      await new Promise(r => setTimeout(r, 450));

      const safeFilename = `Lectura_Tarot_${spread.id}_${Date.now()}.pdf`;

      if (window.html2pdf) {
        const opt = {
          margin: [8, 8, 8, 8],
          filename: safeFilename,
          image: { type: 'jpeg', quality: 0.98 },
          html2canvas: {
            scale: 2,
            useCORS: true,
            logging: false,
            scrollY: 0,
            scrollX: 0
          },
          jsPDF: { unit: 'mm', format: 'a4', orientation: 'portrait' }
        };

        try {
          await window.html2pdf().set(opt).from(targetBox).save();
          showToast('📥', '¡Lectura descargada con éxito!');
          playMysticChime(660);
        } catch (err) {
          console.error('html2pdf spread error:', err);
          showToast('⚠️', 'Abriendo visor para Guardar como PDF...');
          window.print();
        } finally {
          if (document.body.contains(overlay)) {
            document.body.removeChild(overlay);
          }
        }
      } else {
        if (document.body.contains(overlay)) {
          document.body.removeChild(overlay);
        }
        window.print();
      }
    });
  }

  // ==========================================================================
  // TAB 3: BONO 2 - LIBRO Y ORACULO DE COMBINACIONES
  // ==========================================================================
  function setupCombinationsOracle() {
    comboSelectA.innerHTML = '';
    comboSelectB.innerHTML = '';

    TAROT_DB.cards.forEach(card => {
      const optA = document.createElement('option');
      optA.value = card.id;
      optA.textContent = `${card.name} (${card.type === 'Arcano Mayor' ? card.roman : card.suit})`;
      comboSelectA.appendChild(optA);

      const optB = document.createElement('option');
      optB.value = card.id;
      optB.textContent = `${card.name} (${card.type === 'Arcano Mayor' ? card.roman : card.suit})`;
      comboSelectB.appendChild(optB);
    });

    comboSelectA.value = 'la-torre';
    comboSelectB.value = 'la-estrella';

    comboSelectA.addEventListener('change', calculateCombination);
    comboSelectB.addEventListener('change', calculateCombination);

    calculateCombination();
    renderIconicCombos();
  }

  function calculateCombination() {
    const cardA = getCardById(comboSelectA.value);
    const cardB = getCardById(comboSelectB.value);

    // Check if it's one of the predefined iconic pairs
    const iconic = TAROT_DB.combinations.iconic_pairs.find(p => 
      (p.card_a === cardA.id && p.card_b === cardB.id) ||
      (p.card_a === cardB.id && p.card_b === cardA.id)
    );

    if (iconic) {
      comboResultDisplay.innerHTML = `
        <div class="combo-result-card">
          <div class="combo-result-header">
            <h3>🌟 Pareja Clásica: ${iconic.title}</h3>
            <p style="color: var(--gold-light); font-size: 0.95rem; margin-top: 0.25rem;">"${iconic.essence}"</p>
          </div>
          <div class="combo-result-grid">
            <div class="combo-subbox">
              <h4>💖 En el Amor & Pareja</h4>
              <p>${iconic.love}</p>
            </div>
            <div class="combo-subbox">
              <h4>💼 En el Trabajo & Proyectos</h4>
              <p>${iconic.work}</p>
            </div>
            <div class="combo-subbox">
              <h4>🧭 Consejo Maestro de la Unión</h4>
              <p>${iconic.advice}</p>
            </div>
          </div>
        </div>
      `;
      return;
    }

    // Dynamic Synthesis Engine
    const elemA = cardA.element;
    const elemB = cardB.element;

    let elementalDynamic = '';
    if (elemA === elemB) {
      elementalDynamic = `Doble fuerza de ${elemA}: Intensificación directa de la energía elemental de ${elemA}.`;
    } else if ((elemA === 'Fuego' && elemB === 'Aire') || (elemA === 'Aire' && elemB === 'Fuego')) {
      elementalDynamic = 'Fuego + Aire: Las ideas avivan la acción; aceleración rápida y expansión de proyectos.';
    } else if ((elemA === 'Agua' && elemB === 'Tierra') || (elemA === 'Tierra' && elemB === 'Agua')) {
      elementalDynamic = 'Agua + Tierra: Fecundidad fértil; las emociones nutren la materia creando resultados duraderos.';
    } else if ((elemA === 'Fuego' && elemB === 'Agua') || (elemA === 'Agua' && elemB === 'Fuego')) {
      elementalDynamic = 'Fuego + Agua: Tensión de vapor; pasión efervescente que requiere templanza para no evaporarse.';
    } else {
      elementalDynamic = `${elemA} + ${elemB}: Integración complementaria de facultades racionales y prácticas.`;
    }

    comboResultDisplay.innerHTML = `
      <div class="combo-result-card">
        <div class="combo-result-header">
          <h3>Dinámica Combinada: ${cardA.name} + ${cardB.name}</h3>
          <p style="color: var(--gold-light); font-size: 0.92rem; margin-top: 0.25rem;">
            <b>Alquimia Elemental:</b> ${elementalDynamic}
          </p>
        </div>
        <div class="combo-result-grid">
          <div class="combo-subbox">
            <h4>💡 Esencia de la Combinación</h4>
            <p>El arquetipo de <b>${cardA.name}</b> (${cardA.keywords.slice(0, 2).join(', ')}) se fusiona con la energía de <b>${cardB.name}</b> (${cardB.keywords.slice(0, 2).join(', ')}). Momento de actuar integrando ambas lecciones.</p>
          </div>
          <div class="combo-subbox">
            <h4>💖 En el Amor & Relaciones</h4>
            <p>La química entre estas dos cartas pide equilibrar la pasión con la estabilidad y no dejar que los impulsos nublen el compromiso mutuo.</p>
          </div>
          <div class="combo-subbox">
            <h4>💼 En el Trabajo & Finanzas</h4>
            <p>Excelente combinación para resolver problemas mediante un enfoque simultáneo en la estrategia y la acción práctica decidida.</p>
          </div>
        </div>
      </div>
    `;
  }

  function renderIconicCombos() {
    iconicCombosGrid.innerHTML = '';
    TAROT_DB.combinations.iconic_pairs.forEach(pair => {
      const cardA = getCardById(pair.card_a);
      const cardB = getCardById(pair.card_b);

      const node = document.createElement('div');
      node.className = 'map-node';
      node.style.cursor = 'pointer';

      node.innerHTML = `
        <div class="node-header">
          <span class="node-icon">✨</span>
          <span class="node-title">${pair.title}</span>
        </div>
        <div style="display: flex; gap: 0.6rem; margin-bottom: 0.75rem;">
          <img src="${cardA.img}" style="width: 45px; height: 75px; border-radius: 4px; border: 1px solid var(--gold-primary);">
          <img src="${cardB.img}" style="width: 45px; height: 75px; border-radius: 4px; border: 1px solid var(--gold-primary);">
          <div>
            <b style="font-size: 0.86rem; color: var(--gold-light);">${cardA.name} + ${cardB.name}</b>
            <p style="font-size: 0.8rem; color: var(--text-muted); line-height: 1.35; margin-top: 0.2rem;">${pair.essence}</p>
          </div>
        </div>
      `;

      node.addEventListener('click', () => {
        comboSelectA.value = pair.card_a;
        comboSelectB.value = pair.card_b;
        calculateCombination();
        window.scrollTo({ top: 180, behavior: 'smooth' });
      });

      iconicCombosGrid.appendChild(node);
    });
  }

  // ==========================================================================
  // TAB 4: BONO 3 - BARAJA DE ESTUDIO PARA IMPRIMIR
  // ==========================================================================
  function renderPrintableDeck() {
    deckGalleryGrid.innerHTML = '';
    TAROT_DB.cards.forEach(card => {
      const cardBox = document.createElement('div');
      cardBox.style.cssText = 'background: rgba(20, 16, 38, 0.7); border: 1px solid var(--border-subtle); border-radius: 8px; padding: 0.5rem; text-align: center; cursor: pointer; transition: transform 0.2s;';
      cardBox.innerHTML = `
        <img src="${card.img}" style="width: 100%; height: auto; border-radius: 6px; border: 1px solid var(--gold-primary); margin-bottom: 0.35rem;" alt="${card.name}">
        <div style="font-size: 0.75rem; font-weight: 600; color: var(--gold-light); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">${card.name}</div>
      `;

      cardBox.addEventListener('click', () => {
        selectCard(card.id);
        switchTab('tab-mapas');
      });

      deckGalleryGrid.appendChild(cardBox);
    });

    btnPrintDeck.addEventListener('click', () => {
      window.print();
    });
  }

  // ==========================================================================
  // TAB 5: BONO 4 - GUIA PRACTICA DE CARTAS INVERTIDAS
  // ==========================================================================
  function renderInvertedDictionary() {
    invertedDictionaryGrid.innerHTML = '';
    TAROT_DB.cards.forEach(card => {
      const node = document.createElement('div');
      node.className = 'map-node';
      node.style.borderLeft = '3px solid #fb7185';

      node.innerHTML = `
        <div class="node-header">
          <img src="${card.img}" style="width: 32px; height: 55px; border-radius: 4px; border: 1px solid #fb7185; transform: rotate(180deg);">
          <div>
            <div style="font-family: var(--font-serif); font-weight: 700; color: #fca5a5; font-size: 0.98rem;">${card.name} Invertida</div>
            <div style="font-size: 0.74rem; color: var(--text-muted);">${card.reversed.keywords.join(' · ')}</div>
          </div>
        </div>
        <p style="font-size: 0.86rem; color: var(--text-main); margin-bottom: 0.5rem;">${card.reversed.meaning}</p>
        <div style="background: rgba(16, 185, 129, 0.12); padding: 0.45rem 0.65rem; border-radius: 6px; font-size: 0.8rem; color: #34d399;">
          <b>Sanación:</b> ${card.reversed.how_to_heal}
        </div>
      `;

      invertedDictionaryGrid.appendChild(node);
    });
  }

  // ==========================================================================
  // TAB 6: SUPER BONO - APP DE PRACTICA (QUIZ, FLASHCARDS & PROGRESS)
  // ==========================================================================
  practiceCardBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      practiceCardBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      switchPracticeSubmode(btn.dataset.submode);
    });
  });

  function switchPracticeSubmode(mode) {
    Object.keys(practiceSubpanes).forEach(k => {
      practiceSubpanes[k].style.display = (k === mode) ? 'block' : 'none';
    });

    if (mode === 'quiz') renderQuiz();
    if (mode === 'flashcards') renderFlashcard();
    if (mode === 'progress') renderProgressDashboard();
  }

  // Quiz Engine
  function renderQuiz() {
    const questions = TAROT_DB.quiz;
    const qIndex = appState.quizIndex % questions.length;
    const currentQ = questions[qIndex];

    quizContainer.innerHTML = `
      <div class="quiz-score-bar">
        <span>Pregunta ${qIndex + 1} de ${questions.length}</span>
        <span>Aciertos: <b style="color: #34d399;">${appState.quizScore}</b></span>
      </div>

      <div class="quiz-question-text">${currentQ.question}</div>

      <div class="quiz-options-list" id="quiz-options-list">
        ${currentQ.options.map((opt, i) => `
          <button class="quiz-opt-btn" data-index="${i}">
            ${String.fromCharCode(65 + i)}. ${opt}
          </button>
        `).join('')}
      </div>

      <div id="quiz-feedback-container"></div>
    `;

    const optBtns = quizContainer.querySelectorAll('.quiz-opt-btn');
    optBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        handleQuizAnswer(parseInt(btn.dataset.index), currentQ, optBtns);
      });
    });
  }

  function handleQuizAnswer(selectedIndex, currentQ, optBtns) {
    optBtns.forEach(b => b.disabled = true);
    const feedbackEl = document.getElementById('quiz-feedback-container');

    if (selectedIndex === currentQ.correct) {
      optBtns[selectedIndex].classList.add('correct');
      appState.quizScore++;
      playMysticChime(660);
      feedbackEl.innerHTML = `
        <div class="quiz-feedback-box" style="border-color: #10b981;">
          <b style="color: #34d399;">¡Correcto! Excelente intuición.</b>
          <p style="margin-top: 0.25rem;">${currentQ.explanation}</p>
          <button class="btn-deal" style="margin-top: 1rem;" id="btn-next-quiz">Siguiente Pregunta →</button>
        </div>
      `;
    } else {
      optBtns[selectedIndex].classList.add('wrong');
      optBtns[currentQ.correct].classList.add('correct');
      playMysticChime(280);
      feedbackEl.innerHTML = `
        <div class="quiz-feedback-box" style="border-color: #f43f5e;">
          <b style="color: #fb7185;">No del todo. ¡Pero así se aprende!</b>
          <p style="margin-top: 0.25rem;">${currentQ.explanation}</p>
          <button class="btn-deal" style="margin-top: 1rem;" id="btn-next-quiz">Siguiente Pregunta →</button>
        </div>
      `;
    }

    document.getElementById('btn-next-quiz').addEventListener('click', () => {
      appState.quizIndex++;
      saveState();
      renderQuiz();
    });
  }

  // 3D Flashcards Engine
  function renderFlashcard() {
    const card = TAROT_DB.cards[appState.flashcardIndex % TAROT_DB.cards.length];

    flashcardStage.innerHTML = `
      <div style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 0.75rem;">
        Carta ${appState.flashcardIndex + 1} de 78 · Toca para voltear
      </div>

      <div class="flashcard-3d-box" id="flashcard-box">
        <div class="flashcard-inner ${appState.flashcardFlipped ? 'is-flipped' : ''}">
          <div class="flashcard-face flashcard-front">
            <img src="${card.img}" alt="${card.name}">
          </div>
          <div class="flashcard-face flashcard-back">
            <span style="font-size: 0.75rem; color: var(--gold-light); text-transform: uppercase;">${card.type} · ${card.number}</span>
            <h3>${card.name}</h3>
            <p><b>Esencia:</b> "${card.essence}"</p>
            <div style="font-size: 0.82rem; color: #34d399; margin-bottom: 0.4rem;">
              <b>Luz:</b> ${card.light_side.slice(0, 90)}...
            </div>
            <div style="font-size: 0.82rem; color: #fb7185;">
              <b>Sombra:</b> ${card.shadow_side.slice(0, 90)}...
            </div>
          </div>
        </div>
      </div>

      <div class="flashcard-eval-buttons">
        <button class="eval-btn eval-failed" id="btn-fc-hard">⭐ Me Cuesta</button>
        <button class="eval-btn eval-hard" id="btn-fc-next">➡️ Siguiente</button>
        <button class="eval-btn eval-easy" id="btn-fc-easy">✅ La Domino</button>
      </div>
    `;

    document.getElementById('flashcard-box').addEventListener('click', () => {
      appState.flashcardFlipped = !appState.flashcardFlipped;
      document.querySelector('.flashcard-inner').classList.toggle('is-flipped');
      playMysticChime(500);
    });

    document.getElementById('btn-fc-easy').addEventListener('click', () => {
      if (!appState.masteredCards.includes(card.id)) {
        appState.masteredCards.push(card.id);
      }
      appState.difficultCards = appState.difficultCards.filter(c => c !== card.id);
      showToast('✅', `¡${card.name} dominada!`);
      nextFlashcard();
    });

    document.getElementById('btn-fc-hard').addEventListener('click', () => {
      if (!appState.difficultCards.includes(card.id)) {
        appState.difficultCards.push(card.id);
      }
      showToast('⭐', `¡${card.name} en repaso!`);
      nextFlashcard();
    });

    document.getElementById('btn-fc-next').addEventListener('click', () => {
      nextFlashcard();
    });
  }

  function nextFlashcard() {
    appState.flashcardIndex++;
    appState.flashcardFlipped = false;
    saveState();
    renderFlashcard();
    playMysticChime(600);
  }

  // Progress Dashboard
  function renderProgressDashboard() {
    const total = TAROT_DB.cards.length;
    const mastered = appState.masteredCards.length;
    const difficult = appState.difficultCards.length;
    const pct = Math.round((mastered / total) * 100);

    let rankTitle = 'Principiante del Tarot 🥉';
    if (pct >= 90) rankTitle = 'Maestro Supremo del Tarot 👑';
    else if (pct >= 70) rankTitle = 'Tarotista Experto 🔮';
    else if (pct >= 45) rankTitle = 'Iniciado en los Arcanos 🥇';
    else if (pct >= 20) rankTitle = 'Aprendiz Dedicado 🥈';

    progressSummaryGrid.innerHTML = `
      <div class="map-node" style="text-align: center; padding: 2rem;">
        <div style="font-size: 3rem; margin-bottom: 0.5rem;">👑</div>
        <h3 style="font-family: var(--font-serif); font-size: 1.4rem; color: var(--gold-light);">${rankTitle}</h3>
        <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 1.25rem;">Nivel actual de dominio del mazo completo</p>
        
        <div style="background: rgba(0,0,0,0.4); border-radius: 9999px; height: 16px; overflow: hidden; border: 1px solid var(--gold-primary); margin-bottom: 0.75rem;">
          <div style="background: var(--gold-gradient); width: ${pct}%; height: 100%; transition: width 0.6s ease;"></div>
        </div>
        <b style="font-size: 1.2rem; color: var(--gold-light);">${mastered} de ${total} cartas dominadas (${pct}%)</b>
      </div>

      <div class="map-node">
        <div class="node-header">
          <span class="node-icon">📊</span>
          <span class="node-title">Estadísticas de Aprendizaje</span>
        </div>
        <p><b>Cartas Dominadas:</b> <span style="color: #34d399;">${mastered} cartas</span></p>
        <p style="margin-top: 0.5rem;"><b>En Repaso / Difíciles:</b> <span style="color: #f59e0b;">${difficult} cartas</span></p>
        <p style="margin-top: 0.5rem;"><b>Pendientes por aprender:</b> <span style="color: var(--text-muted);">${total - mastered} cartas</span></p>
        <p style="margin-top: 0.5rem;"><b>Aciertos en Quiz:</b> <span style="color: var(--gold-light);">${appState.quizScore} aciertos</span></p>
      </div>

      <div class="map-node" style="grid-column: 1 / -1;">
        <div class="node-header">
          <span class="node-icon">⭐</span>
          <span class="node-title">Tus Cartas en Repaso ("Lo que más te cuesta")</span>
        </div>
        ${difficult === 0 ? 
          '<p style="color: var(--text-muted); font-style: italic;">No tienes cartas marcadas como difíciles. ¡Vas excelente!</p>' : 
          `<div style="display: flex; flex-wrap: wrap; gap: 0.65rem;">
            ${appState.difficultCards.map(id => {
              const c = getCardById(id);
              return `<button class="filter-btn" style="border-color: #f59e0b; color: #fbbf24;" onclick="window.selectCardExternal('${c.id}')">${c.name}</button>`;
            }).join('')}
          </div>`
        }
      </div>
    `;
  }

  // Progress in Header
  function updateProgressDisplay() {
    const total = TAROT_DB.cards.length;
    const mastered = appState.masteredCards.length;
    const pct = Math.round((mastered / total) * 100);
    headerProgressText.textContent = `${mastered}/${total} (${pct}%)`;
  }

  // Expose selectCard for external clicks
  window.selectCardExternal = function(id) {
    selectCard(id);
    switchTab('tab-mapas');
  };

  // ==========================================================================
  // MOBILE CONNECT MODAL (QR & NETWORK ACCESS)
  // ==========================================================================
  const btnMobileModal = document.getElementById('btn-mobile-modal');
  const mobileConnectModal = document.getElementById('mobile-connect-modal');
  const modalCloseBtn = document.getElementById('modal-close-btn');
  const qrCodeImg = document.getElementById('qr-code-img');
  const mobileUrlInput = document.getElementById('mobile-url-input');
  const btnCopyMobileUrl = document.getElementById('btn-copy-mobile-url');

  let detectedMobileUrl = window.location.href;

  // Try to fetch local network IP if served via server.py
  if (window.location.protocol.startsWith('http')) {
    fetch('/api/info')
      .then(r => r.json())
      .then(data => {
        if (data && data.mobile_url && window.location.hostname === 'localhost') {
          detectedMobileUrl = data.mobile_url;
        }
      })
      .catch(() => {});
  }

  function openMobileModal() {
    mobileUrlInput.value = detectedMobileUrl;
    const qrUrl = `https://api.qrserver.com/v1/create-qr-code/?size=220x220&data=${encodeURIComponent(detectedMobileUrl)}`;
    qrCodeImg.src = qrUrl;
    mobileConnectModal.style.display = 'flex';
    playMysticChime(550);
  }

  function closeMobileModal() {
    mobileConnectModal.style.display = 'none';
  }

  if (btnMobileModal) {
    btnMobileModal.addEventListener('click', openMobileModal);
  }

  if (modalCloseBtn) {
    modalCloseBtn.addEventListener('click', closeMobileModal);
  }

  mobileConnectModal.addEventListener('click', (e) => {
    if (e.target === mobileConnectModal) {
      closeMobileModal();
    }
  });

  if (btnCopyMobileUrl) {
    btnCopyMobileUrl.addEventListener('click', () => {
      navigator.clipboard.writeText(detectedMobileUrl).then(() => {
        btnCopyMobileUrl.textContent = '¡Copiado!';
        setTimeout(() => {
          btnCopyMobileUrl.textContent = 'Copiar';
        }, 2000);
      });
    });
  }

  // ==========================================================================
  // INITIALIZATION ON LOAD
  // ==========================================================================
  function init() {
    renderCardsSidebar();
    renderActiveCardView();
    updateMapButtonsState();
    updateMobileNavigator();
    renderSpreadsSelector();
    loadSpreadStage();
    setupCombinationsOracle();
    renderPrintableDeck();
    renderInvertedDictionary();
    renderQuiz();
    renderFlashcard();
    updateProgressDisplay();
  }

  // Run init when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
