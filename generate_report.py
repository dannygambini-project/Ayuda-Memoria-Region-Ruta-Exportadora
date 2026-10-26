import json
import os

with open('regiones_data.json', encoding='utf-8') as f:
    data_json_str = f.read()

html_content = f'''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ayuda Memoria Regional 2026 | PROMPERÚ - Ruta Exportadora</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;1,400&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  
  <style>
    :root {{
      --promperu-red: #C8102E;
      --promperu-red-dark: #9E0B22;
      --promperu-red-light: #FDE8EB;
      --promperu-red-gradient: linear-gradient(135deg, #C8102E 0%, #E61E38 100%);
      --accent-gold: #D4AF37;
      --accent-gold-light: #FFF9E6;
      
      --bg-main: #F4F6F9;
      --bg-surface: #FFFFFF;
      --bg-card: #FFFFFF;
      --bg-elevated: #F8FAFC;
      
      --text-main: #1E293B;
      --text-muted: #64748B;
      --text-light: #94A3B8;
      --text-inverse: #FFFFFF;
      
      --border-subtle: #E2E8F0;
      --border-medium: #CBD5E1;
      
      --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
      --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.07), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
      --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.08), 0 4px 6px -4px rgba(0, 0, 0, 0.04);
      --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.09), 0 8px 10px -6px rgba(0, 0, 0, 0.04);
      --radius-sm: 6px;
      --radius-md: 10px;
      --radius-lg: 16px;
      --radius-full: 9999px;
      
      --transition-normal: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    }}

    * {{
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      -webkit-font-smoothing: antialiased;
    }}

    body {{
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background-color: var(--bg-main);
      color: var(--text-main);
      line-height: 1.6;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }}

    /* Top Institutional Bar */
    .gov-strip {{
      background: #0F172A;
      color: #94A3B8;
      font-size: 0.75rem;
      padding: 6px 2rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid rgba(255,255,255,0.1);
    }}

    .gov-strip .gov-info {{
      display: flex;
      align-items: center;
      gap: 1.25rem;
    }}

    .gov-strip .gov-tag {{
      background: rgba(200, 16, 46, 0.25);
      color: #F87171;
      padding: 2px 8px;
      border-radius: var(--radius-full);
      font-weight: 600;
      letter-spacing: 0.5px;
      text-transform: uppercase;
      font-size: 0.65rem;
    }}

    /* Header */
    header.main-header {{
      background: var(--bg-surface);
      border-bottom: 1px solid var(--border-subtle);
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: var(--shadow-sm);
    }}

    .header-container {{
      max-width: 1440px;
      margin: 0 auto;
      padding: 1rem 2rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 1rem;
    }}

    .brand-group {{
      display: flex;
      align-items: center;
      gap: 1.25rem;
    }}

    .brand-logo-badge {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
      text-decoration: none;
    }}

    .peru-emblem {{
      width: 44px;
      height: 44px;
      background: var(--promperu-red-gradient);
      border-radius: var(--radius-md);
      display: flex;
      align-items: center;
      justify-content: center;
      color: white;
      font-weight: 800;
      font-size: 1.4rem;
      letter-spacing: -0.5px;
      box-shadow: 0 4px 12px rgba(200, 16, 46, 0.35);
    }}

    .brand-text h1 {{
      font-size: 1.25rem;
      font-weight: 800;
      letter-spacing: -0.5px;
      color: var(--promperu-red);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .brand-text h1 span {{
      color: var(--text-main);
      font-weight: 600;
    }}

    .brand-text p {{
      font-size: 0.8rem;
      color: var(--text-muted);
      font-weight: 500;
    }}

    .header-actions {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
      flex-wrap: wrap;
    }}

    /* Buttons */
    .btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.5rem;
      padding: 0.55rem 1.1rem;
      font-size: 0.85rem;
      font-weight: 600;
      border-radius: var(--radius-sm);
      border: 1px solid transparent;
      cursor: pointer;
      transition: var(--transition-normal);
      text-decoration: none;
      white-space: nowrap;
    }}

    .btn-primary {{
      background: var(--promperu-red);
      color: white;
      box-shadow: 0 2px 8px rgba(200, 16, 46, 0.25);
    }}

    .btn-primary:hover {{
      background: var(--promperu-red-dark);
      box-shadow: 0 4px 12px rgba(200, 16, 46, 0.35);
      transform: translateY(-1px);
    }}

    .btn-secondary {{
      background: var(--bg-surface);
      color: var(--text-main);
      border-color: var(--border-medium);
    }}

    .btn-secondary:hover {{
      background: var(--bg-elevated);
      border-color: var(--promperu-red);
      color: var(--promperu-red);
    }}

    .btn-icon {{
      padding: 0.55rem;
    }}

    /* Hero & Filter Panel */
    .hero-panel {{
      background: linear-gradient(180deg, #FFFFFF 0%, #F8FAFC 100%);
      border-bottom: 1px solid var(--border-subtle);
      padding: 1.5rem 2rem;
    }}

    .hero-container {{
      max-width: 1440px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
    }}

    .controls-wrapper {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1.5rem;
      flex-wrap: wrap;
      background: white;
      padding: 1rem 1.25rem;
      border-radius: var(--radius-lg);
      border: 1px solid var(--border-subtle);
      box-shadow: var(--shadow-sm);
    }}

    .region-select-group {{
      display: flex;
      align-items: center;
      gap: 1rem;
      flex: 1;
      min-width: 320px;
    }}

    .region-select-group label {{
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--text-main);
      text-transform: uppercase;
      letter-spacing: 0.5px;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .select-dropdown-container {{
      position: relative;
      flex: 1;
      max-width: 420px;
    }}

    .custom-select {{
      width: 100%;
      padding: 0.65rem 2.5rem 0.65rem 1rem;
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--promperu-red-dark);
      background-color: var(--promperu-red-light);
      border: 1.5px solid #F87171;
      border-radius: var(--radius-md);
      cursor: pointer;
      appearance: none;
      outline: none;
      transition: var(--transition-normal);
    }}

    .custom-select:focus {{
      border-color: var(--promperu-red);
      box-shadow: 0 0 0 3px rgba(200, 16, 46, 0.2);
    }}

    .select-arrow {{
      position: absolute;
      right: 1rem;
      top: 50%;
      transform: translateY(-50%);
      pointer-events: none;
      color: var(--promperu-red);
    }}

    .pills-container {{
      display: flex;
      gap: 0.4rem;
      overflow-x: auto;
      padding-bottom: 4px;
      scrollbar-width: thin;
    }}

    .region-pill {{
      padding: 0.35rem 0.75rem;
      background: white;
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-full);
      font-size: 0.75rem;
      font-weight: 600;
      color: var(--text-muted);
      cursor: pointer;
      transition: var(--transition-normal);
      white-space: nowrap;
    }}

    .region-pill:hover {{
      border-color: var(--promperu-red);
      color: var(--promperu-red);
      background: var(--promperu-red-light);
    }}

    .region-pill.active {{
      background: var(--promperu-red);
      color: white;
      border-color: var(--promperu-red);
      box-shadow: 0 2px 6px rgba(200, 16, 46, 0.3);
    }}

    /* Main Container */
    main.main-content {{
      max-width: 1440px;
      margin: 0 auto;
      padding: 2rem;
      width: 100%;
      flex: 1;
      display: flex;
      flex-direction: column;
      gap: 2rem;
    }}

    /* Official Memo Document View (Paper Style) */
    .official-memo-card {{
      background: white;
      border-radius: var(--radius-lg);
      border: 1px solid var(--border-subtle);
      box-shadow: var(--shadow-lg);
      overflow: hidden;
      position: relative;
    }}

    .official-memo-header {{
      background: linear-gradient(135deg, #FFF5F6 0%, #FFFFFF 100%);
      border-bottom: 2px solid var(--promperu-red);
      padding: 1.5rem 2rem;
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      flex-wrap: wrap;
      gap: 1rem;
    }}

    .official-badge {{
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      background: var(--promperu-red);
      color: white;
      padding: 3px 10px;
      border-radius: var(--radius-full);
      font-size: 0.7rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 0.5rem;
    }}

    .official-memo-header h2 {{
      font-size: 1.35rem;
      font-weight: 800;
      color: #0F172A;
      line-height: 1.3;
    }}

    .official-memo-header .meta-tag {{
      font-size: 0.8rem;
      color: var(--text-muted);
      margin-top: 0.25rem;
    }}

    .memo-actions-toolbar {{
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .official-narrative-box {{
      padding: 2rem;
      background: #FFFFFF;
      position: relative;
    }}

    .narrative-lead {{
      font-size: 1.05rem;
      line-height: 1.8;
      color: #1E293B;
      text-align: justify;
      background: #FDFEFE;
      padding: 1.5rem 1.75rem;
      border-radius: var(--radius-md);
      border-left: 4px solid var(--promperu-red);
      box-shadow: inset 0 0 0 1px rgba(0,0,0,0.03);
    }}

    .narrative-lead strong {{
      color: var(--promperu-red-dark);
      font-weight: 700;
    }}

    .copy-toast {{
      position: fixed;
      bottom: 2rem;
      right: 2rem;
      background: #0F172A;
      color: white;
      padding: 0.75rem 1.5rem;
      border-radius: var(--radius-md);
      font-size: 0.85rem;
      font-weight: 600;
      display: flex;
      align-items: center;
      gap: 0.75rem;
      box-shadow: var(--shadow-xl);
      transform: translateY(100px);
      opacity: 0;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      z-index: 1000;
    }}

    .copy-toast.show {{
      transform: translateY(0);
      opacity: 1;
    }}

    /* KPI Metric Cards Grid */
    .metrics-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 1.25rem;
    }}

    .metric-card {{
      background: white;
      border-radius: var(--radius-md);
      padding: 1.25rem;
      border: 1px solid var(--border-subtle);
      box-shadow: var(--shadow-sm);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: var(--transition-normal);
      position: relative;
      overflow: hidden;
    }}

    .metric-card::before {{
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      width: 4px;
      height: 100%;
      background: var(--border-medium);
      transition: var(--transition-normal);
    }}

    .metric-card:hover {{
      transform: translateY(-2px);
      box-shadow: var(--shadow-md);
      border-color: var(--border-medium);
    }}

    .metric-card.accent-red::before {{
      background: var(--promperu-red);
    }}

    .metric-card.accent-blue::before {{
      background: #0284C7;
    }}

    .metric-card.accent-green::before {{
      background: #059669;
    }}

    .metric-card.accent-purple::before {{
      background: #7C3AED;
    }}

    .metric-card.accent-amber::before {{
      background: #D97706;
    }}

    .metric-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 0.75rem;
    }}

    .metric-title {{
      font-size: 0.8rem;
      font-weight: 700;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}

    .metric-icon {{
      width: 32px;
      height: 32px;
      border-radius: var(--radius-sm);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1rem;
    }}

    .icon-red {{ background: var(--promperu-red-light); color: var(--promperu-red); }}
    .icon-blue {{ background: #E0F2FE; color: #0284C7; }}
    .icon-green {{ background: #ECFDF5; color: #059669; }}
    .icon-purple {{ background: #F3E8FF; color: #7C3AED; }}
    .icon-amber {{ background: #FEF3C7; color: #D97706; }}

    .metric-value {{
      font-size: 1.85rem;
      font-weight: 800;
      color: #0F172A;
      line-height: 1.1;
      margin-bottom: 0.4rem;
    }}

    .metric-subtext {{
      font-size: 0.75rem;
      color: var(--text-muted);
      font-weight: 500;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }}

    /* Section Tabs */
    .tabs-nav {{
      display: flex;
      gap: 0.5rem;
      border-bottom: 2px solid var(--border-subtle);
      overflow-x: auto;
      scrollbar-width: none;
    }}

    .tabs-nav::-webkit-scrollbar {{
      display: none;
    }}

    .tab-btn {{
      padding: 0.75rem 1.25rem;
      background: transparent;
      border: none;
      border-bottom: 3px solid transparent;
      font-size: 0.88rem;
      font-weight: 700;
      color: var(--text-muted);
      cursor: pointer;
      transition: var(--transition-normal);
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      white-space: nowrap;
      margin-bottom: -2px;
    }}

    .tab-btn:hover {{
      color: var(--promperu-red);
    }}

    .tab-btn.active {{
      color: var(--promperu-red);
      border-bottom-color: var(--promperu-red);
      background: rgba(200, 16, 46, 0.04);
      border-radius: var(--radius-sm) var(--radius-sm) 0 0;
    }}

    .tab-badge {{
      background: var(--border-subtle);
      color: var(--text-main);
      padding: 2px 7px;
      border-radius: var(--radius-full);
      font-size: 0.7rem;
      font-weight: 700;
    }}

    .tab-btn.active .tab-badge {{
      background: var(--promperu-red);
      color: white;
    }}

    .tab-content {{
      display: none;
      animation: fadeIn 0.3s ease;
    }}

    .tab-content.active {{
      display: block;
    }}

    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(6px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    /* Tables & Data Cards */
    .content-card {{
      background: white;
      border-radius: var(--radius-lg);
      border: 1px solid var(--border-subtle);
      box-shadow: var(--shadow-sm);
      overflow: hidden;
    }}

    .card-toolbar {{
      padding: 1rem 1.5rem;
      background: #FAFBFD;
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 1rem;
    }}

    .card-toolbar h3 {{
      font-size: 1rem;
      font-weight: 700;
      color: #0F172A;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .search-input-box {{
      position: relative;
      min-width: 250px;
    }}

    .search-input-box input {{
      width: 100%;
      padding: 0.45rem 1rem 0.45rem 2.25rem;
      border: 1px solid var(--border-medium);
      border-radius: var(--radius-sm);
      font-size: 0.8rem;
      outline: none;
      transition: var(--transition-normal);
    }}

    .search-input-box input:focus {{
      border-color: var(--promperu-red);
      box-shadow: 0 0 0 2px rgba(200, 16, 46, 0.15);
    }}

    .search-icon {{
      position: absolute;
      left: 0.75rem;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-light);
      pointer-events: none;
      font-size: 0.85rem;
    }}

    .table-responsive {{
      overflow-x: auto;
      max-height: 520px;
    }}

    table.data-table {{
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 0.85rem;
    }}

    table.data-table th {{
      background: #F1F5F9;
      color: #334155;
      font-weight: 700;
      padding: 0.75rem 1rem;
      border-bottom: 1px solid var(--border-medium);
      position: sticky;
      top: 0;
      z-index: 10;
      white-space: nowrap;
    }}

    table.data-table td {{
      padding: 0.75rem 1rem;
      border-bottom: 1px solid var(--border-subtle);
      color: #334155;
      vertical-align: middle;
    }}

    table.data-table tbody tr:hover {{
      background-color: #F8FAFC;
    }}

    .rank-badge {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 24px;
      height: 24px;
      background: #E2E8F0;
      color: #475569;
      border-radius: var(--radius-full);
      font-size: 0.75rem;
      font-weight: 700;
    }}

    .rank-badge.top-1 {{ background: #FEF3C7; color: #B45309; font-weight: 800; }}
    .rank-badge.top-2 {{ background: #F1F5F9; color: #475569; font-weight: 800; }}
    .rank-badge.top-3 {{ background: #FFEDD5; color: #C2410C; font-weight: 800; }}

    .progress-bar-container {{
      width: 100%;
      max-width: 140px;
      background: #E2E8F0;
      height: 6px;
      border-radius: var(--radius-full);
      overflow: hidden;
      display: inline-block;
      vertical-align: middle;
      margin-right: 0.5rem;
    }}

    .progress-bar-fill {{
      height: 100%;
      background: var(--promperu-red);
      border-radius: var(--radius-full);
    }}

    .progress-bar-fill.blue {{ background: #0284C7; }}
    .progress-bar-fill.green {{ background: #059669; }}

    /* Grid for Markets and Sectors */
    .two-cols-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(450px, 1fr));
      gap: 1.5rem;
    }}

    /* Categorization Badges */
    .cat-badge {{
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      padding: 0.25rem 0.6rem;
      border-radius: var(--radius-full);
      font-size: 0.72rem;
      font-weight: 700;
    }}

    .cat-regular {{ background: #DCFCE7; color: #166534; }}
    .cat-esporadico {{ background: #FEF3C7; color: #92400E; }}
    .cat-nuevas {{ background: #E0E7FF; color: #3730A3; }}
    .cat-no-exporto {{ background: #F1F5F9; color: #475569; }}

    /* Official Word Preview Mode */
    .official-word-sheet {{
      background: white;
      max-width: 850px;
      margin: 1.5rem auto;
      padding: 3.5rem 3rem;
      box-shadow: 0 4px 25px rgba(0, 0, 0, 0.1);
      border: 1px solid var(--border-medium);
      font-family: Arial, sans-serif;
      color: #000000;
      line-height: 1.5;
    }}

    .official-word-sheet h2.word-title {{
      text-align: center;
      font-size: 14pt;
      font-weight: bold;
      margin-bottom: 2rem;
      color: #000000;
    }}

    .official-word-sheet p.word-paragraph {{
      font-size: 11pt;
      text-align: justify;
      margin-bottom: 1.5rem;
      color: #000000;
    }}

    .official-word-sheet h3.word-subtitle {{
      font-size: 11pt;
      font-weight: bold;
      margin-top: 1.5rem;
      margin-bottom: 1rem;
      color: #000000;
    }}

    .official-word-sheet ul.word-bullet-list {{
      list-style-type: disc;
      padding-left: 2rem;
      margin-bottom: 1.5rem;
    }}

    .official-word-sheet ul.word-bullet-list li {{
      font-size: 11pt;
      margin-bottom: 0.5rem;
      color: #000000;
    }}

    /* All Regions Comparative Table */
    .all-regions-modal {{
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(15, 23, 42, 0.7);
      backdrop-filter: blur(4px);
      z-index: 200;
      padding: 2rem;
      overflow-y: auto;
    }}

    .all-regions-modal.show {{
      display: flex;
      align-items: center;
      justify-content: center;
    }}

    .modal-dialog {{
      background: white;
      border-radius: var(--radius-lg);
      max-width: 1100px;
      width: 100%;
      max-height: 90vh;
      display: flex;
      flex-direction: column;
      box-shadow: var(--shadow-xl);
      overflow: hidden;
    }}

    .modal-header {{
      padding: 1.25rem 1.75rem;
      background: #FAFBFD;
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .modal-header h3 {{
      font-size: 1.15rem;
      font-weight: 800;
      color: #0F172A;
    }}

    .modal-close {{
      background: transparent;
      border: none;
      font-size: 1.5rem;
      cursor: pointer;
      color: var(--text-muted);
    }}

    .modal-close:hover {{
      color: var(--promperu-red);
    }}

    .modal-body {{
      padding: 1.5rem;
      overflow-y: auto;
    }}

    /* Footer */
    footer.main-footer {{
      background: white;
      border-top: 1px solid var(--border-subtle);
      padding: 2rem;
      margin-top: auto;
      font-size: 0.8rem;
      color: var(--text-muted);
    }}

    .footer-container {{
      max-width: 1440px;
      margin: 0 auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 1rem;
    }}

    /* Print Stylesheet */
    @media print {{
      .gov-strip,
      header.main-header,
      .hero-panel,
      .memo-actions-toolbar,
      .tabs-nav,
      .tab-content:not(#tab-oficial),
      .card-toolbar,
      .copy-toast,
      .all-regions-modal,
      footer.main-footer,
      .no-print {{
        display: none !important;
      }}

      body {{
        background: white !important;
        color: black !important;
        font-size: 11pt;
      }}

      main.main-content {{
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
      }}

      .official-memo-card {{
        border: none !important;
        box-shadow: none !important;
      }}

      .tab-content#tab-oficial {{
        display: block !important;
      }}

      .official-word-sheet {{
        border: none !important;
        box-shadow: none !important;
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
      }}

      @page {{
        margin: 2cm;
        size: A4 portrait;
      }}
    }}

    /* Responsive */
    @media (max-width: 768px) {{
      .header-container {{
        flex-direction: column;
        align-items: flex-start;
      }}
      .controls-wrapper {{
        flex-direction: column;
        align-items: stretch;
      }}
      .region-select-group {{
        min-width: 100%;
      }}
      .select-dropdown-container {{
        max-width: 100%;
      }}
      .two-cols-grid {{
        grid-template-columns: 1fr;
      }}
      .official-word-sheet {{
        padding: 1.5rem 1rem;
      }}
    }}
  </style>
</head>
<body>

  <!-- Top Gov Info Strip -->
  <div class="gov-strip">
    <div class="gov-info">
      <span><strong>GOBIERNO DEL PERÚ</strong> | Ministerio de Comercio Exterior y Turismo (MINCETUR)</span>
      <span class="gov-tag">Uso Oficial</span>
    </div>
    <div class="gov-status">
      <span>Ruta Exportadora 2026 | Sistema de Inteligencia Regional</span>
    </div>
  </div>

  <!-- Institutional Header -->
  <header class="main-header">
    <div class="header-container">
      <div class="brand-group">
        <div class="brand-logo-badge">
          <div class="peru-emblem">P</div>
          <div class="brand-text">
            <h1>PROMPERÚ <span>| Dirección de las Regiones</span></h1>
            <p>Subdirección de Desarrollo Exportador &bull; Reporte de Ayudas Memorias Regionales</p>
          </div>
        </div>
      </div>

      <div class="header-actions">
        <button class="btn btn-secondary" id="btn-all-regions" title="Ver matriz comparativa nacional">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="3" rx="2"/><path d="M3 9h18"/><path d="M9 21V9"/></svg>
          Comparativa Nacional
        </button>
        <button class="btn btn-secondary" id="btn-copy-memo" title="Copiar texto completo al portapapeles">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="14" height="14" x="8" y="8" rx="2" ry="2"/><path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2"/></svg>
          Copiar Texto
        </button>
        <button class="btn btn-secondary" id="btn-download-word" title="Descargar documento en formato Word (.docx)">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><line x1="10" y1="9" x2="8" y2="9"/></svg>
          Descargar Word (.docx)
        </button>
        <button class="btn btn-primary" id="btn-download-pdf" title="Imprimir o guardar como PDF oficial">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9V2h12v7"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect width="12" height="8" x="6" y="14"/></svg>
          Imprimir / PDF
        </button>
      </div>
    </div>
  </header>

  <!-- Interactive Filter Bar -->
  <div class="hero-panel">
    <div class="hero-container">
      <div class="controls-wrapper">
        <div class="region-select-group">
          <label for="select-region">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg>
            Seleccionar Región:
          </label>
          <div class="select-dropdown-container">
            <select id="select-region" class="custom-select">
              <!-- Dynamically populated -->
            </select>
            <div class="select-arrow">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg>
            </div>
          </div>
        </div>

        <div class="pills-container" id="region-pills-list">
          <!-- Dynamically populated regional pills -->
        </div>
      </div>
    </div>
  </div>

  <!-- Main Content Body -->
  <main class="main-content">

    <!-- Official Ayuda Memoria Card (Executive Box) -->
    <section class="official-memo-card">
      <div class="official-memo-header">
        <div>
          <span class="official-badge">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>
            Documento de Ayuda Memoria Oficial
          </span>
          <h2 id="memo-title">Ayuda memoria de las atenciones de la Ruta Exportadora en Amazonas 2026</h2>
          <div class="meta-tag">Periodo analizado: Año 2026 &bull; Fuente: Bases RUTEX, Categorías & Exportaciones SUNAT</div>
        </div>
        <div class="memo-actions-toolbar">
          <button class="btn btn-secondary btn-icon" id="btn-quick-copy" title="Copiar párrafo de síntesis">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="14" height="14" x="8" y="8" rx="2" ry="2"/><path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2"/></svg>
          </button>
        </div>
      </div>

      <div class="official-narrative-box">
        <div class="narrative-lead" id="memo-narrative">
          <!-- Dynamically populated narrative -->
        </div>
      </div>
    </section>

    <!-- Executive KPI Grid -->
    <section class="metrics-grid">
      <!-- Total Empresas -->
      <div class="metric-card accent-red">
        <div class="metric-header">
          <span class="metric-title">Empresas Atendidas</span>
          <div class="metric-icon icon-red">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
          </div>
        </div>
        <div class="metric-value" id="kpi-empresas">0</div>
        <div class="metric-subtext" id="kpi-empresas-sub">RUCs únicos atendidos en 2026</div>
      </div>

      <!-- Actividades / Eventos -->
      <div class="metric-card accent-blue">
        <div class="metric-header">
          <span class="metric-title">Actividades Realizadas</span>
          <div class="metric-icon icon-blue">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="4" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
          </div>
        </div>
        <div class="metric-value" id="kpi-eventos">0</div>
        <div class="metric-subtext" id="kpi-eventos-sub">0 en Lima &bull; 0 en regiones</div>
      </div>

      <!-- Empresas Exportadoras -->
      <div class="metric-card accent-green">
        <div class="metric-header">
          <span class="metric-title">Empresas Exportadoras</span>
          <div class="metric-icon icon-green">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="m4.93 4.93 4.24 4.24"/><path d="m14.83 9.17 4.24-4.24"/><path d="m14.83 14.83 4.24 4.24"/><path d="m9.17 14.83-4.24 4.24"/></svg>
          </div>
        </div>
        <div class="metric-value" id="kpi-exportadoras">0</div>
        <div class="metric-subtext" id="kpi-exportadoras-sub">0% de tasa de exportación regional</div>
      </div>

      <!-- Mercados y Productos -->
      <div class="metric-card accent-purple">
        <div class="metric-header">
          <span class="metric-title">Mercados / Productos</span>
          <div class="metric-icon icon-purple">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>
          </div>
        </div>
        <div class="metric-value" id="kpi-mercados-prods">0 / 0</div>
        <div class="metric-subtext" id="kpi-mercados-sub">Mercados destino / Subpartidas</div>
      </div>

      <!-- Monto FOB Total -->
      <div class="metric-card accent-amber">
        <div class="metric-header">
          <span class="metric-title">Exportaciones FOB</span>
          <div class="metric-icon icon-amber">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
          </div>
        </div>
        <div class="metric-value" id="kpi-fob">USD 0 M</div>
        <div class="metric-subtext" id="kpi-fob-sub">Valor exportado por empresas atendidas</div>
      </div>
    </section>

    <!-- Navigation Tabs for Detailed Sections -->
    <nav class="tabs-nav">
      <button class="tab-btn active" data-tab="tab-atenciones">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>
        Principales Atenciones
        <span class="tab-badge" id="badge-count-atenciones">0</span>
      </button>

      <button class="tab-btn" data-tab="tab-productos">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>
        Productos Exportados
        <span class="tab-badge" id="badge-count-productos">0</span>
      </button>

      <button class="tab-btn" data-tab="tab-mercados">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
        Mercados de Destino
        <span class="tab-badge" id="badge-count-mercados">0</span>
      </button>

      <button class="tab-btn" data-tab="tab-sectores">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect width="18" height="18" x="3" y="3" rx="2"/><path d="M3 9h18"/><path d="M9 21V9"/></svg>
        Sectores & Categorías
      </button>

      <button class="tab-btn" data-tab="tab-oficial">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1-2.5-2.5Z"/><path d="M6 6h10"/><path d="M6 10h10"/></svg>
        Formato Word Oficial (Minuta)
      </button>
    </nav>

    <!-- Tab 1: Principales Atenciones -->
    <div class="tab-content active" id="tab-atenciones">
      <div class="content-card">
        <div class="card-toolbar">
          <h3>
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="color: var(--promperu-red)"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
            Ranking de Principales Atenciones y Eventos Recibidos en 2026
          </h3>
          <div class="search-input-box">
            <span class="search-icon">🔍</span>
            <input type="text" id="search-atenciones" placeholder="Filtrar eventos o capacitaciones...">
          </div>
        </div>
        <div class="table-responsive">
          <table class="data-table" id="table-atenciones">
            <thead>
              <tr>
                <th style="width: 60px;">#</th>
                <th>Nombre del Evento / Actividad de PromPerú</th>
                <th style="width: 140px; text-align: center;">Empresas</th>
                <th style="width: 180px;">Impacto</th>
              </tr>
            </thead>
            <tbody>
              <!-- Dynamic rows -->
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- Tab 2: Productos Exportados -->
    <div class="tab-content" id="tab-productos">
      <div class="content-card">
        <div class="card-toolbar">
          <h3>
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="color: var(--promperu-red)"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>
            Principales Subpartidas Arancelarias y Productos Exportados (2025/2026)
          </h3>
          <div class="search-input-box">
            <span class="search-icon">🔍</span>
            <input type="text" id="search-productos" placeholder="Filtrar por producto o código...">
          </div>
        </div>
        <div class="table-responsive">
          <table class="data-table" id="table-productos">
            <thead>
              <tr>
                <th style="width: 60px;">#</th>
                <th>Descripción Arancelaria del Producto</th>
                <th style="width: 150px; text-align: right;">Monto FOB (USD)</th>
                <th style="width: 130px; text-align: right;">USD Millones</th>
                <th style="width: 160px;">Participación</th>
              </tr>
            </thead>
            <tbody>
              <!-- Dynamic rows -->
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- Tab 3: Mercados de Destino -->
    <div class="tab-content" id="tab-mercados">
      <div class="content-card">
        <div class="card-toolbar">
          <h3>
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="color: var(--promperu-red)"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
            Principales Mercados Internacionales de Destino
          </h3>
          <div class="search-input-box">
            <span class="search-icon">🔍</span>
            <input type="text" id="search-mercados" placeholder="Filtrar por país o mercado...">
          </div>
        </div>
        <div class="table-responsive">
          <table class="data-table" id="table-mercados">
            <thead>
              <tr>
                <th style="width: 60px;">#</th>
                <th>Mercado / País de Destino</th>
                <th style="width: 150px; text-align: right;">Monto FOB (USD)</th>
                <th style="width: 130px; text-align: right;">USD Millones</th>
                <th style="width: 160px;">Participación</th>
              </tr>
            </thead>
            <tbody>
              <!-- Dynamic rows -->
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- Tab 4: Sectores y Categorías -->
    <div class="tab-content" id="tab-sectores">
      <div class="two-cols-grid">
        <!-- Sectores Económicos -->
        <div class="content-card">
          <div class="card-toolbar">
            <h3>Distribución Sectorial de Empresas Atendidas</h3>
          </div>
          <div class="table-responsive">
            <table class="data-table" id="table-sectores">
              <thead>
                <tr>
                  <th>Sector Económico</th>
                  <th style="width: 110px; text-align: center;">Empresas</th>
                  <th style="width: 100px; text-align: right;">% Part.</th>
                  <th style="width: 130px;">Distribución</th>
                </tr>
              </thead>
              <tbody>
                <!-- Dynamic rows -->
              </tbody>
            </table>
          </div>
        </div>

        <!-- Categorización 2025 -->
        <div class="content-card">
          <div class="card-toolbar">
            <h3>Categorización de Empresas Atendidas (2025)</h3>
          </div>
          <div class="table-responsive">
            <table class="data-table" id="table-categorias">
              <thead>
                <tr>
                  <th>Categoría Oficial</th>
                  <th style="width: 110px; text-align: center;">Empresas</th>
                  <th style="width: 100px; text-align: right;">% Part.</th>
                  <th style="width: 130px;">Clasificación</th>
                </tr>
              </thead>
              <tbody>
                <!-- Dynamic rows -->
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>

    <!-- Tab 5: Formato Word Oficial (Minuta) -->
    <div class="tab-content" id="tab-oficial">
      <div class="official-word-sheet" id="word-sheet-preview">
        <h2 class="word-title" id="word-sheet-title">Ayuda memoria de las atenciones de la Ruta Exportadora en Amazonas 2026</h2>
        <p class="word-paragraph" id="word-sheet-p1"></p>
        <h3 class="word-subtitle" id="word-sheet-subtitle">Las principales atenciones recibidas en el 2026 son:</h3>
        <ul class="word-bullet-list" id="word-sheet-bullets">
          <!-- Dynamically populated bullet items -->
        </ul>
      </div>
    </div>

  </main>

  <!-- Modal: All Regions Comparison Matrix -->
  <div class="all-regions-modal" id="modal-all-regions">
    <div class="modal-dialog">
      <div class="modal-header">
        <div>
          <h3>Matriz Nacional de Regiones - Ruta Exportadora 2026</h3>
          <p style="font-size: 0.8rem; color: var(--text-muted);">Comparativa de las 25 regiones del Perú</p>
        </div>
        <button class="modal-close" id="btn-close-modal">&times;</button>
      </div>
      <div class="modal-body">
        <div style="margin-bottom: 1rem;">
          <input type="text" id="search-modal-region" placeholder="Buscar región..." style="width: 100%; padding: 0.5rem 1rem; border: 1px solid var(--border-medium); border-radius: var(--radius-sm); font-size: 0.85rem;">
        </div>
        <div class="table-responsive">
          <table class="data-table" id="table-all-regions">
            <thead>
              <tr>
                <th>Región</th>
                <th style="text-align: center;">Empresas</th>
                <th style="text-align: center;">Eventos</th>
                <th style="text-align: center;">Exportadoras</th>
                <th style="text-align: center;">Mercados</th>
                <th style="text-align: center;">Productos</th>
                <th style="text-align: right;">FOB (USD Mill.)</th>
                <th style="text-align: center;">Acción</th>
              </tr>
            </thead>
            <tbody>
              <!-- Dynamic rows -->
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>

  <!-- Toast Notification -->
  <div class="copy-toast" id="copy-toast">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="color: #4ADE80"><polyline points="20 6 9 17 4 12"/></svg>
    <span id="copy-toast-text">Texto copiado al portapapeles con éxito</span>
  </div>

  <!-- Institutional Footer -->
  <footer class="main-footer">
    <div class="footer-container">
      <div>
        <strong>Comisión de Promoción del Perú para la Exportación y el Turismo - PROMPERÚ</strong><br>
        Dirección de las Regiones | Subdirección de Desarrollo Exportador &bull; Lima, Perú
      </div>
      <div>
        Sistema de Ayuda Memoria Automatizado &bull; Versión Web 100% Frontend (Sin dependencias externas)
      </div>
    </div>
  </footer>

  <!-- EMBEDDED COMPLETE REGIONAL DATASET (Preprocessed from RUTEX, Categorías y Exportaciones 2025) -->
  <script>
    const REGIONES_DATA = {data_json_str};
  </script>

  <!-- JAVASCRIPT LOGIC & INTERACTION ENGINE -->
  <script>
    (function() {{
      // State
      let currentRegionId = 'amazonas';
      const regionsMap = REGIONES_DATA.regiones || {{}};

      // DOM Elements
      const selectRegion = document.getElementById('select-region');
      const regionPillsList = document.getElementById('region-pills-list');
      const memoTitle = document.getElementById('memo-title');
      const memoNarrative = document.getElementById('memo-narrative');
      
      // KPIs
      const kpiEmpresas = document.getElementById('kpi-empresas');
      const kpiEmpresasSub = document.getElementById('kpi-empresas-sub');
      const kpiEventos = document.getElementById('kpi-eventos');
      const kpiEventosSub = document.getElementById('kpi-eventos-sub');
      const kpiExportadoras = document.getElementById('kpi-exportadoras');
      const kpiExportadorasSub = document.getElementById('kpi-exportadoras-sub');
      const kpiMercadosProds = document.getElementById('kpi-mercados-prods');
      const kpiMercadosSub = document.getElementById('kpi-mercados-sub');
      const kpiFob = document.getElementById('kpi-fob');
      const kpiFobSub = document.getElementById('kpi-fob-sub');

      // Badges
      const badgeCountAtenciones = document.getElementById('badge-count-atenciones');
      const badgeCountProductos = document.getElementById('badge-count-productos');
      const badgeCountMercados = document.getElementById('badge-count-mercados');

      // Tables
      const tableAtencionesBody = document.querySelector('#table-atenciones tbody');
      const tableProductosBody = document.querySelector('#table-productos tbody');
      const tableMercadosBody = document.querySelector('#table-mercados tbody');
      const tableSectoresBody = document.querySelector('#table-sectores tbody');
      const tableCategoriasBody = document.querySelector('#table-categorias tbody');

      // Word Sheet Preview
      const wordSheetTitle = document.getElementById('word-sheet-title');
      const wordSheetP1 = document.getElementById('word-sheet-p1');
      const wordSheetSubtitle = document.getElementById('word-sheet-subtitle');
      const wordSheetBullets = document.getElementById('word-sheet-bullets');

      // Modal
      const modalAllRegions = document.getElementById('modal-all-regions');
      const btnAllRegions = document.getElementById('btn-all-regions');
      const btnCloseModal = document.getElementById('btn-close-modal');
      const tableAllRegionsBody = document.querySelector('#table-all-regions tbody');
      const searchModalRegion = document.getElementById('search-modal-region');

      // Buttons
      const btnCopyMemo = document.getElementById('btn-copy-memo');
      const btnQuickCopy = document.getElementById('btn-quick-copy');
      const btnDownloadWord = document.getElementById('btn-download-word');
      const btnDownloadPdf = document.getElementById('btn-download-pdf');
      const copyToast = document.getElementById('copy-toast');
      const copyToastText = document.getElementById('copy-toast-text');

      // Search Inputs
      const searchAtenciones = document.getElementById('search-atenciones');
      const searchProductos = document.getElementById('search-productos');
      const searchMercados = document.getElementById('search-mercados');

      // Tab Buttons
      const tabButtons = document.querySelectorAll('.tab-btn');
      const tabContents = document.querySelectorAll('.tab-content');

      // Helper: Show Toast
      function showToast(message) {{
        copyToastText.textContent = message;
        copyToast.classList.add('show');
        setTimeout(() => {{
          copyToast.classList.remove('show');
        }}, 3000);
      }}

      // Initialize Dropdown and Pills
      function initRegionSelectors() {{
        selectRegion.innerHTML = '';
        regionPillsList.innerHTML = '';

        const sortedRegions = Object.values(regionsMap).sort((a, b) => a.nombre.localeCompare(b.nombre));

        sortedRegions.forEach(reg => {{
          // Dropdown option
          const opt = document.createElement('option');
          opt.value = reg.id;
          opt.textContent = `${{reg.nombre}} (${{reg.total_empresas}} empresas)`;
          selectRegion.appendChild(opt);

          // Pill button
          const pill = document.createElement('button');
          pill.className = 'region-pill';
          pill.dataset.id = reg.id;
          pill.textContent = reg.nombre;
          pill.addEventListener('click', () => setRegion(reg.id));
          regionPillsList.appendChild(pill);
        }});

        selectRegion.addEventListener('change', (e) => {{
          setRegion(e.target.value);
        }});
      }}

      // Switch Active Region
      function setRegion(regionId) {{
        if (!regionsMap[regionId]) return;
        currentRegionId = regionId;

        // Update dropdown
        selectRegion.value = regionId;

        // Update pills active state
        document.querySelectorAll('.region-pill').forEach(pill => {{
          pill.classList.toggle('active', pill.dataset.id === regionId);
          if (pill.dataset.id === regionId) {{
            pill.scrollIntoView({{ behavior: 'smooth', block: 'nearest', inline: 'center' }});
          }}
        }});

        renderRegionData(regionsMap[regionId]);
      }}

      // Render Region Data
      function renderRegionData(reg) {{
        // Titles and Narrative
        const titleText = `Ayuda memoria de las atenciones de la Ruta Exportadora en ${{reg.nombre}} ${{reg.anio}}`;
        memoTitle.textContent = titleText;
        memoNarrative.innerHTML = formatNarrativeHTML(reg.parrafo_narrativa, reg);

        // Word Sheet Preview
        wordSheetTitle.textContent = titleText;
        wordSheetP1.textContent = reg.parrafo_narrativa;
        wordSheetSubtitle.textContent = `Las principales atenciones recibidas en el ${{reg.anio}} son:`;
        wordSheetBullets.innerHTML = '';
        reg.atenciones.forEach(item => {{
          const li = document.createElement('li');
          const empStr = item.empresas === 1 ? 'empresa' : 'empresas';
          li.textContent = `${{item.evento}} a ${{item.empresas}} ${{empStr}}`;
          wordSheetBullets.appendChild(li);
        }});

        // KPI Cards
        kpiEmpresas.textContent = reg.total_empresas.toLocaleString();
        kpiEmpresasSub.textContent = `RUCs únicos atendidos en ${{reg.anio}}`;

        kpiEventos.textContent = reg.eventos_unicos.toLocaleString();
        kpiEventosSub.textContent = `${{reg.evt_lima}} en Lima • ${{reg.evt_regiones}} en regiones`;

        kpiExportadoras.textContent = reg.cant_exportadoras.toLocaleString();
        const exportRate = reg.total_empresas > 0 ? Math.round((reg.cant_exportadoras / reg.total_empresas) * 100) : 0;
        kpiExportadorasSub.textContent = `${{exportRate}}% de tasa de exportación regional`;

        kpiMercadosProds.textContent = `${{reg.cant_mercados}} / ${{reg.cant_productos}}`;
        kpiMercadosSub.textContent = `Mercados destino / Subpartidas`;

        kpiFob.textContent = `USD ${{reg.monto_fob_display}} M`;
        kpiFobSub.textContent = `Valor exportado por empresas atendidas`;

        // Tab Badges
        badgeCountAtenciones.textContent = reg.atenciones.length;
        badgeCountProductos.textContent = reg.productos.length;
        badgeCountMercados.textContent = reg.mercados.length;

        // Render Tables
        renderAtencionesTable(reg.atenciones, reg.total_empresas);
        renderProductosTable(reg.productos);
        renderMercadosTable(reg.mercados);
        renderSectoresTable(reg.sectores, reg.total_empresas);
        renderCategoriasTable(reg.categorias, reg.total_empresas);

        // Reset search inputs
        searchAtenciones.value = '';
        searchProductos.value = '';
        searchMercados.value = '';
      }}

      // Format Narrative with Highlights
      function formatNarrativeHTML(text, reg) {{
        if (!text) return '';
        let formatted = text;
        formatted = formatted.replace(new RegExp(`\\\\b${{reg.nombre}}\\\\b`, 'gi'), `<strong>${{reg.nombre}}</strong>`);
        formatted = formatted.replace(new RegExp(`\\\\b${{reg.total_empresas}} empresas\\\\b`, 'gi'), `<strong>${{reg.total_empresas}} empresas</strong>`);
        formatted = formatted.replace(new RegExp(`\\\\b${{reg.cant_exportadoras}} exportaron\\\\b`, 'gi'), `<strong>${{reg.cant_exportadoras}} exportaron</strong>`);
        formatted = formatted.replace(new RegExp(`USD ${{reg.monto_fob_display}} millones`, 'gi'), `<strong>USD ${{reg.monto_fob_display}} millones</strong>`);
        return formatted;
      }}

      // Render Tab 1: Atenciones
      function renderAtencionesTable(atenciones, totalEmpresas) {{
        tableAtencionesBody.innerHTML = '';
        if (!atenciones || atenciones.length === 0) {{
          tableAtencionesBody.innerHTML = `<tr><td colspan="4" style="text-align:center; padding: 2rem; color: var(--text-muted);">No se registran actividades para esta región</td></tr>`;
          return;
        }}

        const maxEmp = Math.max(...atenciones.map(a => a.empresas), 1);

        atenciones.forEach((item, index) => {{
          const tr = document.createElement('tr');
          const rankClass = index === 0 ? 'top-1' : index === 1 ? 'top-2' : index === 2 ? 'top-3' : '';
          const empStr = item.empresas === 1 ? 'empresa' : 'empresas';
          const pct = Math.round((item.empresas / maxEmp) * 100);

          tr.innerHTML = `
            <td><span class="rank-badge ${{rankClass}}">${{index + 1}}</span></td>
            <td><strong>${{item.evento}}</strong></td>
            <td style="text-align: center;"><span style="font-weight: 700; color: var(--promperu-red);">${{item.empresas}}</span> ${{empStr}}</td>
            <td>
              <div class="progress-bar-container">
                <div class="progress-bar-fill" style="width: ${{pct}}%;"></div>
              </div>
              <span style="font-size: 0.75rem; color: var(--text-muted);">${{pct}}% rel.</span>
            </td>
          `;
          tableAtencionesBody.appendChild(tr);
        }});
      }}

      // Render Tab 2: Productos
      function renderProductosTable(productos) {{
        tableProductosBody.innerHTML = '';
        if (!productos || productos.length === 0) {{
          tableProductosBody.innerHTML = `<tr><td colspan="5" style="text-align:center; padding: 2rem; color: var(--text-muted);">Sin productos destacados exportados</td></tr>`;
          return;
        }}

        productos.forEach((item, index) => {{
          const tr = document.createElement('tr');
          const rankClass = index === 0 ? 'top-1' : index === 1 ? 'top-2' : index === 2 ? 'top-3' : '';
          tr.innerHTML = `
            <td><span class="rank-badge ${{rankClass}}">${{index + 1}}</span></td>
            <td>
              <div style="font-weight: 700; color: #0F172A;">${{item.producto}}</div>
              <div style="font-size: 0.75rem; color: var(--text-muted);">${{item.partida_completa}}</div>
            </td>
            <td style="text-align: right; font-family: 'JetBrains Mono', monospace;">USD ${{item.fob_usd.toLocaleString(undefined, {{minimumFractionDigits: 0, maximumFractionDigits: 0}})}}</td>
            <td style="text-align: right; font-weight: 700; color: var(--promperu-red); font-family: 'JetBrains Mono', monospace;">USD ${{item.fob_millones.toFixed(1)}} M</td>
            <td>
              <div class="progress-bar-container">
                <div class="progress-bar-fill blue" style="width: ${{Math.min(item.participacion, 100)}}%;"></div>
              </div>
              <span style="font-size: 0.75rem; font-weight: 600;">${{item.participacion}}%</span>
            </td>
          `;
          tableProductosBody.appendChild(tr);
        }});
      }}

      // Render Tab 3: Mercados
      function renderMercadosTable(mercados) {{
        tableMercadosBody.innerHTML = '';
        if (!mercados || mercados.length === 0) {{
          tableMercadosBody.innerHTML = `<tr><td colspan="5" style="text-align:center; padding: 2rem; color: var(--text-muted);">Sin mercados destacados registrados</td></tr>`;
          return;
        }}

        mercados.forEach((item, index) => {{
          const tr = document.createElement('tr');
          const rankClass = index === 0 ? 'top-1' : index === 1 ? 'top-2' : index === 2 ? 'top-3' : '';
          tr.innerHTML = `
            <td><span class="rank-badge ${{rankClass}}">${{index + 1}}</span></td>
            <td><strong>${{item.mercado}}</strong></td>
            <td style="text-align: right; font-family: 'JetBrains Mono', monospace;">USD ${{item.fob_usd.toLocaleString(undefined, {{minimumFractionDigits: 0, maximumFractionDigits: 0}})}}</td>
            <td style="text-align: right; font-weight: 700; color: var(--promperu-red); font-family: 'JetBrains Mono', monospace;">USD ${{item.fob_millones.toFixed(1)}} M</td>
            <td>
              <div class="progress-bar-container">
                <div class="progress-bar-fill green" style="width: ${{Math.min(item.participacion, 100)}}%;"></div>
              </div>
              <span style="font-size: 0.75rem; font-weight: 600;">${{item.participacion}}%</span>
            </td>
          `;
          tableMercadosBody.appendChild(tr);
        }});
      }}

      // Render Tab 4: Sectores
      function renderSectoresTable(sectores, totalEmpresas) {{
        tableSectoresBody.innerHTML = '';
        if (!sectores || sectores.length === 0) {{
          tableSectoresBody.innerHTML = `<tr><td colspan="4" style="text-align:center; padding: 2rem; color: var(--text-muted);">Sin sectores registrados</td></tr>`;
          return;
        }}

        sectores.forEach(sec => {{
          const tr = document.createElement('tr');
          tr.innerHTML = `
            <td><strong>${{sec.sector}}</strong></td>
            <td style="text-align: center; font-weight: 700;">${{sec.cantidad}}</td>
            <td style="text-align: right; font-weight: 700; color: var(--promperu-red);">${{sec.porcentaje}}%</td>
            <td>
              <div class="progress-bar-container">
                <div class="progress-bar-fill" style="width: ${{Math.min(sec.porcentaje, 100)}}%;"></div>
              </div>
            </td>
          `;
          tableSectoresBody.appendChild(tr);
        }});
      }}

      // Render Tab 4: Categorías
      function renderCategoriasTable(categorias, totalEmpresas) {{
        tableCategoriasBody.innerHTML = '';
        if (!categorias) return;

        const catStyles = {{
          'Regular': 'cat-regular',
          'Esporádico': 'cat-esporadico',
          'Nuevas': 'cat-nuevas',
          'No exportó': 'cat-no-exporto',
          'Sin categoría': 'cat-no-exporto'
        }};

        Object.entries(categorias).forEach(([catName, count]) => {{
          const pct = totalEmpresas > 0 ? Math.round((count / totalEmpresas) * 100) : 0;
          const tr = document.createElement('tr');
          const badgeStyle = catStyles[catName] || 'cat-no-exporto';

          tr.innerHTML = `
            <td><strong>${{catName}}</strong></td>
            <td style="text-align: center; font-weight: 700;">${{count}}</td>
            <td style="text-align: right; font-weight: 700;">${{pct}}%</td>
            <td><span class="cat-badge ${{badgeStyle}}">${{catName}}</span></td>
          `;
          tableCategoriasBody.appendChild(tr);
        }});
      }}

      // Render All Regions Modal Matrix
      function renderAllRegionsTable(filterText = '') {{
        tableAllRegionsBody.innerHTML = '';
        const normFilter = filterText.toLowerCase().trim();

        const sorted = Object.values(regionsMap).sort((a, b) => a.nombre.localeCompare(b.nombre));

        sorted.forEach(reg => {{
          if (normFilter && !reg.nombre.toLowerCase().includes(normFilter)) {{
            return;
          }}

          const tr = document.createElement('tr');
          tr.innerHTML = `
            <td><strong>${{reg.nombre}}</strong></td>
            <td style="text-align: center; font-weight: 700;">${{reg.total_empresas}}</td>
            <td style="text-align: center;">${{reg.eventos_unicos}}</td>
            <td style="text-align: center; color: #059669; font-weight: 700;">${{reg.cant_exportadoras}}</td>
            <td style="text-align: center;">${{reg.cant_mercados}}</td>
            <td style="text-align: center;">${{reg.cant_productos}}</td>
            <td style="text-align: right; font-weight: 700; color: var(--promperu-red); font-family: 'JetBrains Mono', monospace;">USD ${{reg.monto_fob_display}} M</td>
            <td style="text-align: center;">
              <button class="btn btn-secondary" style="padding: 2px 8px; font-size: 0.75rem;" onclick="window.selectRegionFromModal('${{reg.id}}')">Ver</button>
            </td>
          `;
          tableAllRegionsBody.appendChild(tr);
        }});
      }}

      window.selectRegionFromModal = function(regId) {{
        modalAllRegions.classList.remove('show');
        setRegion(regId);
      }};

      // Search filters for tables
      searchAtenciones.addEventListener('input', (e) => {{
        const q = e.target.value.toLowerCase().trim();
        const rows = tableAtencionesBody.querySelectorAll('tr');
        rows.forEach(r => {{
          r.style.display = r.textContent.toLowerCase().includes(q) ? '' : 'none';
        }});
      }});

      searchProductos.addEventListener('input', (e) => {{
        const q = e.target.value.toLowerCase().trim();
        const rows = tableProductosBody.querySelectorAll('tr');
        rows.forEach(r => {{
          r.style.display = r.textContent.toLowerCase().includes(q) ? '' : 'none';
        }});
      }});

      searchMercados.addEventListener('input', (e) => {{
        const q = e.target.value.toLowerCase().trim();
        const rows = tableMercadosBody.querySelectorAll('tr');
        rows.forEach(r => {{
          r.style.display = r.textContent.toLowerCase().includes(q) ? '' : 'none';
        }});
      }});

      searchModalRegion.addEventListener('input', (e) => {{
        renderAllRegionsTable(e.target.value);
      }});

      // Tab Switching
      tabButtons.forEach(btn => {{
        btn.addEventListener('click', () => {{
          const tabId = btn.dataset.tab;
          tabButtons.forEach(b => b.classList.remove('active'));
          tabContents.forEach(c => c.classList.remove('active'));

          btn.classList.add('active');
          document.getElementById(tabId).classList.add('active');
        }});
      }});

      // Copy Complete Memo Text
      function copyMemoToClipboard() {{
        const reg = regionsMap[currentRegionId];
        if (!reg) return;

        let bulletsText = '';
        reg.atenciones.forEach(item => {{
          const empStr = item.empresas === 1 ? 'empresa' : 'empresas';
          bulletsText += `• ${{item.evento}} a ${{item.empresas}} ${{empStr}}\\n`;
        }});

        const fullText = `${{reg.titulo_documento}}\\n\\n${{reg.parrafo_narrativa}}\\n\\n${{reg.parrafo_atenciones_header}}\\n${{bulletsText}}`;

        navigator.clipboard.writeText(fullText).then(() => {{
          showToast(`¡Ayuda memoria de ${{reg.nombre}} copiada al portapapeles!`);
        }}).catch(() => {{
          // Fallback
          const textarea = document.createElement('textarea');
          textarea.value = fullText;
          document.body.appendChild(textarea);
          textarea.select();
          document.execCommand('copy');
          document.body.removeChild(textarea);
          showToast(`¡Ayuda memoria de ${{reg.nombre}} copiada al portapapeles!`);
        }});
      }}

      btnCopyMemo.addEventListener('click', copyMemoToClipboard);
      btnQuickCopy.addEventListener('click', copyMemoToClipboard);

      // Helper to convert base64 to Blob
      function base64ToBlob(base64, mimeType) {{
        const byteCharacters = atob(base64);
        const byteArrays = [];
        const sliceSize = 1024;
        for (let offset = 0; offset < byteCharacters.length; offset += sliceSize) {{
          const slice = byteCharacters.slice(offset, offset + sliceSize);
          const byteNumbers = new Array(slice.length);
          for (let i = 0; i < slice.length; i++) {{
            byteNumbers[i] = slice.charCodeAt(i);
          }}
          byteArrays.push(new Uint8Array(byteNumbers));
        }}
        return new Blob(byteArrays, {{ type: mimeType }});
      }}

      // Download Word Document (.docx)
      btnDownloadWord.addEventListener('click', () => {{
        const reg = regionsMap[currentRegionId];
        if (!reg) return;

        const docxFileName = `Ayuda memoria de las atenciones de la Ruta Exportadora en ${{reg.nombre}} ${{reg.anio}}.docx`;

        if (reg.docx_base64) {{
          const blob = base64ToBlob(reg.docx_base64, 'application/vnd.openxmlformats-officedocument.wordprocessingml.document');
          const url = URL.createObjectURL(blob);
          const a = document.createElement('a');
          a.href = url;
          a.download = docxFileName;
          document.body.appendChild(a);
          a.click();
          document.body.removeChild(a);
          setTimeout(() => URL.revokeObjectURL(url), 2000);
          showToast(`¡Documento Word (.docx) descargado con éxito!`);
          return;
        }}

        let atencionesHtml = '';
        reg.atenciones.forEach(item => {{
          const empStr = item.empresas === 1 ? 'empresa' : 'empresas';
          atencionesHtml += `<li style="font-family: Arial, sans-serif; font-size: 11pt; margin-bottom: 4pt;">${{item.evento}} a ${{item.empresas}} ${{empStr}}</li>`;
        }});

        const wordDocContent = `
          <html xmlns:o='urn:schemas-microsoft-com:office:office' xmlns:w='urn:schemas-microsoft-com:office:word' xmlns='http://www.w3.org/TR/REC-html40'>
          <head>
            <meta charset='utf-8'>
            <title>${{reg.titulo_documento}}</title>
            <style>
              body {{ font-family: 'Arial', sans-serif; font-size: 11pt; line-height: 1.5; color: #000000; margin: 2cm; }}
              h1.word-title {{ font-size: 14pt; font-weight: bold; text-align: center; margin-bottom: 24pt; }}
              p.word-p {{ font-size: 11pt; text-align: justify; margin-bottom: 14pt; }}
              h2.word-h2 {{ font-size: 11pt; font-weight: bold; margin-top: 18pt; margin-bottom: 8pt; }}
              ul.word-list {{ margin-left: 20pt; }}
            </style>
          </head>
          <body>
            <h1 class="word-title">${{reg.titulo_documento}}</h1>
            <p class="word-p">${{reg.parrafo_narrativa}}</p>
            <h2 class="word-h2">${{reg.parrafo_atenciones_header}}</h2>
            <ul class="word-list">${{atencionesHtml}}</ul>
          </body>
          </html>
        `;

        const blob = new Blob(['\\ufeff' + wordDocContent], {{ type: 'application/msword' }});
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = docxFileName;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
        showToast(`Documento Word para ${{reg.nombre}} generado.`);
      }});

      // Print / PDF View
      btnDownloadPdf.addEventListener('click', () => {{
        // Ensure official tab is visible for printing
        const officialTabBtn = document.querySelector('.tab-btn[data-tab="tab-oficial"]');
        if (officialTabBtn) {{
          officialTabBtn.click();
        }}
        setTimeout(() => {{
          window.print();
        }}, 200);
      }});

      // Modal handlers
      btnAllRegions.addEventListener('click', () => {{
        renderAllRegionsTable();
        modalAllRegions.classList.add('show');
      }});

      btnCloseModal.addEventListener('click', () => {{
        modalAllRegions.classList.remove('show');
      }});

      modalAllRegions.addEventListener('click', (e) => {{
        if (e.target === modalAllRegions) {{
          modalAllRegions.classList.remove('show');
        }}
      }});

      // Keyboard shortcuts
      document.addEventListener('keydown', (e) => {{
        if (e.key === 'Escape' && modalAllRegions.classList.contains('show')) {{
          modalAllRegions.classList.remove('show');
        }}
      }});

      // Initialize on Load
      initRegionSelectors();
      setRegion('amazonas');

    }})();
  </script>
</body>
</html>
'''

# Write reporte_promperu.html
with open('reporte_promperu.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

# Also write index.html as a drop-in copy
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

# Also write reporte_ayuda_memoria_regional_2026.html
with open('reporte_ayuda_memoria_regional_2026.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Generated reporte_promperu.html, index.html, and reporte_ayuda_memoria_regional_2026.html successfully!")
