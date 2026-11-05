/* ==========================================================================
   78 MAPAS VISUALES DEL TAROT - SISTEMA Y LOGICA DE LA PLATAFORMA
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

  // DOM Elements cache
  const navTabsContainer = document.getElementById('nav-tabs-container');
  const tabPanes = document.querySelectorAll('.tab-pane');
  const cardsScrollList = document.getElementById('cards-scroll-list');
  const cardViewContainer = document.getElementById('card-view-container');
  const mapFilterPills = document.getElementById('map-filter-pills');
  const globalSearchInput = document.getElementById('global-search-input');
  const headerProgressText = document.getElementById('header-progress-text');
  const headerProgressPill = document.getElementById('header-progress-pill');

  // Map Controls
  const btnStarCard = document.getElementById('btn-star-card');
  const btnCheckCard = document.getElementById('btn-check-card');
  const btnPrintMap = document.getElementById('btn-print-map');

  // Spreads Elements
  const spreadsSelectorBar = document.getElementById('spreads-selector-bar');
  const activeSpreadTitle = document.getElementById('active-spread-title');
  const matSlotsArea = document.getElementById('mat-slots-area');
  const btnDealSpread = document.getElementById('btn-deal-spread');
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
  // NAVIGATION & TAB SWITCHING
  // ==========================================================================
  function switchTab(targetTabId) {
    document.querySelectorAll('.nav-btn').forEach(btn => {
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
    } else {
      appState.masteredCards.push(id);
      // If mastered, remove from difficult
      appState.difficultCards = appState.difficultCards.filter(c => c !== id);
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
    } else {
      appState.difficultCards.push(id);
      playMysticChime(380);
    }
    saveState();
    updateMapButtonsState();
    renderCardsSidebar();
  });

  btnPrintMap.addEventListener('click', () => {
    // Switch to sheet mode momentarily for clean printing
    const prevMode = appState.mapViewMode;
    appState.mapViewMode = 'sheet';
    renderActiveCardView();
    window.print();
    setTimeout(() => {
      appState.mapViewMode = prevMode;
      renderActiveCardView();
    }, 500);
  });

  // Render the selected card according to active mode
  function renderActiveCardView() {
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

    const keywordsBadges = card.keywords.map(k => `
      <span class="badge-tag tag-gold">${k}</span>
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

  // VISTA 2: FICHA DE ESTUDIO RESUMEN A4
  function renderSheetView(card) {
    const wrapper = document.createElement('div');
    wrapper.className = 'sheet-container';

    const symbolsList = card.symbols.map(s => `
      <li><b>${s.name}:</b> ${s.desc}</li>
    `).join('');

    wrapper.innerHTML = `
      <div class="sheet-header">
        <img class="sheet-card-img" src="${card.img}" alt="${card.name}">
        <div class="sheet-title-box">
          <span style="font-size: 0.8rem; font-weight: 700; color: #786b99; text-transform: uppercase;">
            ${card.type} · ${card.number} · Elemento ${card.element}
          </span>
          <h2>${card.name}</h2>
          <div class="sheet-keywords">${card.keywords.join(' · ')}</div>
          <div class="sheet-essence"><b>Esencia:</b> "${card.essence}"</div>
        </div>
        <div style="text-align: right; font-size: 0.75rem; color: #888;">
          <div>78 Mapas Mentales del Tarot</div>
          <div>Ficha de Consulta Rápida A4</div>
        </div>
      </div>

      <div class="sheet-grid">
        <div class="sheet-box">
          <h3>👁️ Símbolos Visuales Clave</h3>
          <ul style="padding-left: 1.15rem; display: flex; flex-direction: column; gap: 0.4rem;">
            ${symbolsList}
          </ul>
        </div>

        <div class="sheet-box">
          <h3>⚖️ Lado Luz y Lado Sombra</h3>
          <div style="margin-bottom: 0.75rem;">
            <b style="color: #059669;">☀️ Lado Luz:</b>
            <p>${card.light_side}</p>
          </div>
          <div>
            <b style="color: #e11d48;">🌑 Lado Sombra:</b>
            <p>${card.shadow_side}</p>
          </div>
        </div>

        <div class="sheet-box">
          <h3>💖 Amor y Relaciones</h3>
          <p>${card.love}</p>
          <h3 style="margin-top: 1rem;">💼 Trabajo y Finanzas</h3>
          <p>${card.work}</p>
        </div>

        <div class="sheet-box">
          <h3>🧭 Consejo & Carta Invertida</h3>
          <div style="margin-bottom: 0.75rem;">
            <b>Acción Recomendada:</b>
            <p>${card.advice}</p>
          </div>
          <div style="margin-bottom: 0.75rem;">
            <b>Pregunta de Autoindagación:</b>
            <p style="font-style: italic;">"${card.reflection_question}"</p>
          </div>
          <div style="background: #fdf2f4; border-left: 3px solid #e11d48; padding: 0.5rem 0.75rem; border-radius: 4px;">
            <b style="color: #be123c;">🔄 Al salir invertida:</b>
            <p style="font-size: 0.84rem;">${card.reversed.meaning}</p>
          </div>
        </div>
      </div>
    `;

    cardViewContainer.appendChild(wrapper);
  }

  // VISTA 3: GUIA DE LECTURA PROFUNDA
  function renderGuideView(card) {
    const wrapper = document.createElement('div');
    wrapper.style.cssText = 'max-width: 850px; margin: 0 auto; line-height: 1.7;';

    wrapper.innerHTML = `
      <div style="display: flex; gap: 1.5rem; align-items: center; margin-bottom: 2rem; border-bottom: 1px solid var(--border-subtle); padding-bottom: 1.5rem;">
        <img src="${card.img}" style="width: 100px; height: 170px; border-radius: 6px; border: 1px solid var(--gold-primary);" alt="${card.name}">
        <div>
          <span style="font-size: 0.8rem; color: var(--gold-light); text-transform: uppercase;">${card.type} · ${card.number}</span>
          <h2 style="font-family: var(--font-serif); font-size: 2rem; color: var(--text-main);">${card.name}</h2>
          <p style="color: var(--text-muted); font-size: 0.95rem;">${card.keywords.join(' · ')}</p>
        </div>
      </div>

      <div style="display: flex; flex-direction: column; gap: 1.5rem;">
        <div>
          <h3 style="font-family: var(--font-serif); color: var(--gold-light); margin-bottom: 0.5rem;">Significado General al Derecho</h3>
          <p style="color: var(--text-main);">${card.meaning_upright}</p>
        </div>

        <div>
          <h3 style="font-family: var(--font-serif); color: var(--gold-light); margin-bottom: 0.5rem;">La Simbología Esotérica de la Carta</h3>
          <div style="display: flex; flex-direction: column; gap: 0.5rem;">
            ${card.symbols.map(s => `<p><b>${s.name}:</b> ${s.desc}</p>`).join('')}
          </div>
        </div>

        <div>
          <h3 style="font-family: var(--font-serif); color: var(--gold-light); margin-bottom: 0.5rem;">Dimensiones Vitales de Consulta</h3>
          <p><b>En el Amor:</b> ${card.love}</p>
          <p style="margin-top: 0.5rem;"><b>En el Trabajo y Dinero:</b> ${card.work}</p>
          <p style="margin-top: 0.5rem;"><b>En la Espiritualidad:</b> ${card.spirituality}</p>
        </div>

        <div style="background: rgba(244, 63, 94, 0.1); border-left: 3px solid var(--accent-rose); padding: 1rem; border-radius: 6px;">
          <h3 style="font-family: var(--font-serif); color: #fb7185; margin-bottom: 0.4rem;">Interpretación en Posición Invertida</h3>
          <p style="margin-bottom: 0.5rem;">${card.reversed.meaning}</p>
          <p><b>Cómo sanar esta energía:</b> ${card.reversed.how_to_heal}</p>
        </div>
      </div>
    `;

    cardViewContainer.appendChild(wrapper);
  }

  // ==========================================================================
  // TAB 2: BONO 1 - GUIA DE 12 TIRADAS & SIMULADOR EN VIVO
  // ==========================================================================
  let spreadDealtCards = []; // { card, isReversed, isFlipped }

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
          Las ${spread.card_count} cartas han sido colocadas en el tapete. <b>Haz clic sobre cualquier carta</b> para revelarla y leer su mensaje para esa posición.
        </p>
      </div>
    `;
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
  }

  // ==========================================================================
  // TAB 3: BONO 2 - LIBRO Y ORACULO DE COMBINACIONES
  // ==========================================================================
  function setupCombinationsOracle() {
    // Populate dropdowns
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
      nextFlashcard();
    });

    document.getElementById('btn-fc-hard').addEventListener('click', () => {
      if (!appState.difficultCards.includes(card.id)) {
        appState.difficultCards.push(card.id);
      }
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

  let detectedMobileUrl = `http://${window.location.hostname || 'localhost'}:8000`;

  // Fetch local network IP from server API if available
  fetch('/api/info')
    .then(r => r.json())
    .then(data => {
      if (data && data.mobile_url) {
        detectedMobileUrl = data.mobile_url;
      }
    })
    .catch(() => {
      // If running without server.py, keep hostname or default
      if (window.location.hostname && window.location.hostname !== 'localhost' && window.location.hostname !== '127.0.0.1') {
        detectedMobileUrl = window.location.href;
      }
    });

  function openMobileModal() {
    mobileUrlInput.value = detectedMobileUrl;
    // Generate QR code pointing to the mobile URL
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

