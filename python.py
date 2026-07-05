html_code = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>TechNova — Technology That Helps Your Business Grow Smarter</title>
<meta name="description" content="We build intelligent software solutions that automate processes, improve productivity, and help organizations thrive in the digital age.">
<meta property="og:title" content="TechNova — Technology That Helps Your Business Grow Smarter">
<meta property="og:description" content="Intelligent software solutions for schools, businesses, churches, and government institutions.">
<meta property="og:type" content="website">
<style>
  :root {
    --deep-blue: #0A4DFF;
    --purple: #6C4EFF;
    --cyan: #00D4FF;
    --white: #FFFFFF;
    --light-gray: #F4F6FA;
    --medium-gray: #8892A0;
    --dark-gray: #1A1D2E;
    --near-black: #0B0E1A;
    --glass-bg: rgba(255,255,255,0.08);
    --glass-border: rgba(255,255,255,0.12);
    --shadow-sm: 0 2px 8px rgba(0,0,0,0.06);
    --shadow-md: 0 8px 30px rgba(0,0,0,0.08);
    --shadow-lg: 0 20px 60px rgba(0,0,0,0.12);
    --radius-sm: 12px;
    --radius-md: 20px;
    --radius-lg: 28px;
  }

  * { margin: 0; padding: 0; box-sizing: border-box; }
  html { scroll-behavior: smooth; }
  body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    background: var(--white);
    color: var(--dark-gray);
    line-height: 1.6;
    overflow-x: hidden;
    -webkit-font-smoothing: antialiased;
  }

  @keyframes float {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-20px); }
  }
  @keyframes floatSlow {
    0%, 100% { transform: translateY(0px) rotate(0deg); }
    50% { transform: translateY(-30px) rotate(3deg); }
  }
  @keyframes pulseGlow {
    0%, 100% { opacity: 0.4; transform: scale(1); }
    50% { opacity: 0.7; transform: scale(1.05); }
  }
  @keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
  }
  @keyframes fadeInUp {
    from { opacity: 0; transform: translateY(40px); }
    to { opacity: 1; transform: translateY(0); }
  }

  .animate-on-scroll {
    opacity: 0;
    transform: translateY(40px);
    transition: opacity 0.8s cubic-bezier(0.16, 1, 0.3, 1), transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
  }
  .animate-on-scroll.visible {
    opacity: 1;
    transform: translateY(0);
  }
  .delay-1 { transition-delay: 0.1s; }
  .delay-2 { transition-delay: 0.2s; }
  .delay-3 { transition-delay: 0.3s; }
  .delay-4 { transition-delay: 0.4s; }

  .navbar {
    position: fixed;
    top: 0; left: 0; right: 0;
    z-index: 1000;
    padding: 16px 0;
    transition: all 0.4s ease;
    background: transparent;
  }
  .navbar.scrolled {
    background: rgba(255,255,255,0.85);
    backdrop-filter: blur(20px) saturate(180%);
    -webkit-backdrop-filter: blur(20px) saturate(180%);
    box-shadow: var(--shadow-sm);
    padding: 12px 0;
  }
  .nav-container {
    max-width: 1280px;
    margin: 0 auto;
    padding: 0 24px;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  .logo {
    font-size: 1.5rem;
    font-weight: 800;
    color: var(--white);
    text-decoration: none;
    display: flex;
    align-items: center;
    gap: 10px;
    transition: color 0.3s;
  }
  .navbar.scrolled .logo { color: var(--deep-blue); }
  .logo-icon {
    width: 36px; height: 36px;
    background: linear-gradient(135deg, var(--deep-blue), var(--purple));
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-weight: 700;
    font-size: 1rem;
  }
  .nav-links {
    display: flex;
    gap: 32px;
    list-style: none;
    align-items: center;
  }
  .nav-links a {
    text-decoration: none;
    color: rgba(255,255,255,0.8);
    font-size: 0.9rem;
    font-weight: 500;
    transition: color 0.3s;
    position: relative;
  }
  .navbar.scrolled .nav-links a { color: var(--dark-gray); }
  .nav-links a::after {
    content: '';
    position: absolute;
    bottom: -4px; left: 0;
    width: 0; height: 2px;
    background: linear-gradient(90deg, var(--deep-blue), var(--cyan));
    transition: width 0.3s ease;
  }
  .nav-links a:hover::after { width: 100%; }
  .nav-links a:hover { color: var(--white); }
  .navbar.scrolled .nav-links a:hover { color: var(--deep-blue); }
  .nav-cta {
    background: linear-gradient(135deg, var(--deep-blue), var(--purple));
    color: white !important;
    padding: 10px 24px;
    border-radius: 50px;
    font-weight: 600;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(10,77,255,0.3);
  }
  .nav-cta:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(10,77,255,0.4);
  }
  .nav-cta::after { display: none !important; }
  .mobile-toggle {
    display: none;
    background: none;
    border: none;
    cursor: pointer;
    padding: 8px;
  }
  .mobile-toggle span {
    display: block;
    width: 24px; height: 2px;
    background: white;
    margin: 5px 0;
    transition: 0.3s;
    border-radius: 2px;
  }
  .navbar.scrolled .mobile-toggle span { background: var(--dark-gray); }

  .hero {
    position: relative;
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    background: var(--near-black);
  }
  .hero-bg {
    position: absolute;
    inset: 0;
    background:
      radial-gradient(ellipse 80% 60% at 20% 40%, rgba(10,77,255,0.15) 0%, transparent 60%),
      radial-gradient(ellipse 60% 50% at 80% 60%, rgba(108,78,255,0.12) 0%, transparent 60%),
      radial-gradient(ellipse 50% 40% at 50% 100%, rgba(0,212,255,0.08) 0%, transparent 50%),
      var(--near-black);
  }
  .hero-grid {
    position: absolute;
    inset: 0;
    background-image:
      linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px),
      linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px);
    background-size: 60px 60px;
    mask-image: radial-gradient(ellipse 70% 70% at 50% 50%, black 30%, transparent 70%);
    -webkit-mask-image: radial-gradient(ellipse 70% 70% at 50% 50%, black 30%, transparent 70%);
  }
  .hero-orb {
    position: absolute;
    border-radius: 50%;
    filter: blur(80px);
    pointer-events: none;
  }
  .orb-1 {
    width: 400px; height: 400px;
    background: rgba(10,77,255,0.2);
    top: 10%; left: 10%;
    animation: floatSlow 8s ease-in-out infinite;
  }
  .orb-2 {
    width: 300px; height: 300px;
    background: rgba(108,78,255,0.15);
    top: 50%; right: 15%;
    animation: floatSlow 10s ease-in-out infinite reverse;
  }
  .orb-3 {
    width: 250px; height: 250px;
    background: rgba(0,212,255,0.1);
    bottom: 15%; left: 40%;
    animation: floatSlow 12s ease-in-out infinite;
  }
  .hero-content {
    position: relative;
    z-index: 2;
    text-align: center;
    max-width: 900px;
    padding: 0 24px;
  }
  .hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 8px 20px;
    background: var(--glass-bg);
    border: 1px solid var(--glass-border);
    border-radius: 50px;
    color: var(--cyan);
    font-size: 0.85rem;
    font-weight: 500;
    margin-bottom: 32px;
    backdrop-filter: blur(10px);
    animation: fadeInUp 0.8s ease-out 0.2s both;
  }
  .hero-badge::before {
    content: '';
    width: 8px; height: 8px;
    background: var(--cyan);
    border-radius: 50%;
    animation: pulseGlow 2s ease-in-out infinite;
  }
  .hero h1 {
    font-size: clamp(2.5rem, 6vw, 4.5rem);
    font-weight: 800;
    line-height: 1.1;
    color: white;
    margin-bottom: 24px;
    letter-spacing: -0.03em;
    animation: fadeInUp 0.8s ease-out 0.4s both;
  }
  .hero h1 .gradient-text {
    background: linear-gradient(135deg, var(--deep-blue), var(--cyan), var(--purple));
    background-size: 200% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: gradientShift 4s ease infinite;
  }
  .hero-sub {
    font-size: clamp(1rem, 2vw, 1.25rem);
    color: rgba(255,255,255,0.65);
    max-width: 640px;
    margin: 0 auto 40px;
    line-height: 1.7;
    animation: fadeInUp 0.8s ease-out 0.6s both;
  }
  .hero-cta-group {
    display: flex;
    gap: 16px;
    justify-content: center;
    flex-wrap: wrap;
    animation: fadeInUp 0.8s ease-out 0.8s both;
  }
  .btn {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    padding: 16px 36px;
    border-radius: 50px;
    font-size: 1rem;
    font-weight: 600;
    text-decoration: none;
    transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    cursor: pointer;
    border: none;
    position: relative;
    overflow: hidden;
  }
  .btn-primary {
    background: linear-gradient(135deg, var(--deep-blue), var(--purple));
    color: white;
    box-shadow: 0 8px 30px rgba(10,77,255,0.35);
  }
  .btn-primary:hover {
    transform: translateY(-3px);
    box-shadow: 0 12px 40px rgba(10,77,255,0.45);
  }
  .btn-secondary {
    background: var(--glass-bg);
    color: white;
    border: 1px solid var(--glass-border);
    backdrop-filter: blur(10px);
  }
  .btn-secondary:hover {
    background: rgba(255,255,255,0.15);
    transform: translateY(-3px);
  }
  .hero-scroll {
    position: absolute;
    bottom: 40px;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 8px;
    color: rgba(255,255,255,0.4);
    font-size: 0.8rem;
    animation: fadeInUp 1s ease-out 1.2s both;
  }
  .scroll-line {
    width: 1px;
    height: 40px;
    background: linear-gradient(to bottom, var(--cyan), transparent);
    animation: float 2s ease-in-out infinite;
  }

  .trusted {
    padding: 60px 0;
    background: var(--white);
    border-bottom: 1px solid rgba(0,0,0,0.05);
  }
  .trusted-inner {
    max-width: 1280px;
    margin: 0 auto;
    padding: 0 24px;
    text-align: center;
  }
  .trusted-label {
    font-size: 0.8rem;
    font-weight: 600;
    color: var(--medium-gray);
    text-transform: uppercase;
    letter-spacing: 0.15em;
    margin-bottom: 32px;
  }
  .logos-grid {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 48px;
    flex-wrap: wrap;
    opacity: 0.5;
  }
  .logo-placeholder {
    font-size: 1.1rem;
    font-weight: 700;
    color: var(--medium-gray);
    letter-spacing: -0.02em;
    transition: all 0.3s;
    filter: grayscale(100%);
  }
  .logo-placeholder:hover {
    opacity: 1;
    filter: grayscale(0%);
    color: var(--deep-blue);
  }

  section {
    padding: 100px 0;
  }
  .container {
    max-width: 1280px;
    margin: 0 auto;
    padding: 0 24px;
  }
  .section-header {
    text-align: center;
    max-width: 640px;
    margin: 0 auto 64px;
  }
  .section-tag {
    display: inline-block;
    padding: 6px 16px;
    background: linear-gradient(135deg, rgba(10,77,255,0.08), rgba(108,78,255,0.08));
    border-radius: 50px;
    color: var(--deep-blue);
    font-size: 0.8rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-bottom: 16px;
  }
  .section-title {
    font-size: clamp(2rem, 4vw, 3rem);
    font-weight: 800;
    color: var(--near-black);
    line-height: 1.15;
    letter-spacing: -0.03em;
    margin-bottom: 16px;
  }
  .section-desc {
    font-size: 1.1rem;
    color: var(--medium-gray);
    line-height: 1.7;
  }

  .about {
    background: var(--light-gray);
  }
  .about-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 64px;
    align-items: center;
  }
  .about-visual {
    position: relative;
  }
  .about-visual .glass-card {
    background: linear-gradient(135deg, rgba(10,77,255,0.05), rgba(108,78,255,0.05));
    border: 1px solid rgba(10,77,255,0.1);
    border-radius: var(--radius-lg);
    padding: 48px;
    position: relative;
    overflow: hidden;
  }
  .about-visual .glass-card::before {
    content: '';
    position: absolute;
    top: -50%; left: -50%;
    width: 200%; height: 200%;
    background: radial-gradient(circle, rgba(10,77,255,0.08) 0%, transparent 70%);
    animation: pulseGlow 6s ease-in-out infinite;
  }
  .about-visual h3 {
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--near-black);
    margin-bottom: 16px;
    position: relative;
  }
  .about-visual p {
    color: var(--medium-gray);
    position: relative;
  }
  .about-text h3 {
    font-size: 1.3rem;
    font-weight: 700;
    color: var(--near-black);
    margin-bottom: 12px;
  }
  .about-text p {
    color: var(--medium-gray);
    margin-bottom: 24px;
    line-height: 1.8;
  }
  .about-mission {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 24px;
    margin-top: 32px;
  }
  .mission-card {
    background: white;
    border-radius: var(--radius-md);
    padding: 28px;
    box-shadow: var(--shadow-sm);
    transition: all 0.3s ease;
  }
  .mission-card:hover {
    transform: translateY(-4px);
    box-shadow: var(--shadow-md);
  }
  .mission-card .icon {
    width: 44px; height: 44px;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 16px;
    font-size: 1.2rem;
  }
  .mission-card:nth-child(1) .icon { background: rgba(10,77,255,0.1); color: var(--deep-blue); }
  .mission-card:nth-child(2) .icon { background: rgba(108,78,255,0.1); color: var(--purple); }
  .mission-card:nth-child(3) .icon { background: rgba(0,212,255,0.1); color: var(--cyan); }
  .mission-card:nth-child(4) .icon { background: rgba(10,77,255,0.1); color: var(--deep-blue); }

  .products-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 28px;
  }
  .product-card {
    background: white;
    border-radius: var(--radius-lg);
    overflow: hidden;
    box-shadow: var(--shadow-sm);
    transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    border: 1px solid rgba(0,0,0,0.04);
    position: relative;
  }
  .product-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 4px;
    background: linear-gradient(90deg, var(--deep-blue), var(--purple), var(--cyan));
    opacity: 0;
    transition: opacity 0.3s;
  }
  .product-card:hover::before { opacity: 1; }
  .product-card:hover {
    transform: translateY(-8px);
    box-shadow: var(--shadow-lg);
  }
  .product-img {
    height: 200px;
    background: linear-gradient(135deg, var(--light-gray), #E8ECF4);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 3rem;
    position: relative;
    overflow: hidden;
  }
  .product-img::after {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(135deg, rgba(10,77,255,0.05), rgba(108,78,255,0.05));
  }
  .product-info { padding: 28px; }
  .product-info h3 {
    font-size: 1.2rem;
    font-weight: 700;
    color: var(--near-black);
    margin-bottom: 8px;
  }
  .product-info p {
    color: var(--medium-gray);
    font-size: 0.95rem;
    margin-bottom: 20px;
    line-height: 1.6;
  }
  .product-link {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    color: var(--deep-blue);
    font-weight: 600;
    font-size: 0.9rem;
    text-decoration: none;
    transition: gap 0.3s;
  }
  .product-link:hover { gap: 12px; }

  .services {
    background: var(--near-black);
    position: relative;
    overflow: hidden;
  }
  .services .section-title { color: white; }
  .services .section-desc { color: rgba(255,255,255,0.5); }
  .services .section-tag {
    background: rgba(255,255,255,0.08);
    color: var(--cyan);
  }
  .services-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 20px;
  }
  .service-card {
    background: var(--glass-bg);
    border: 1px solid var(--glass-border);
    border-radius: var(--radius-md);
    padding: 32px;
    transition: all 0.4s ease;
    position: relative;
    overflow: hidden;
  }
  .service-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background: linear-gradient(135deg, rgba(10,77,255,0.1), rgba(108,78,255,0.1));
    opacity: 0;
    transition: opacity 0.4s;
  }
  .service-card:hover::before { opacity: 1; }
  .service-card:hover {
    transform: translateY(-4px);
    border-color: rgba(10,77,255,0.3);
  }
  .service-card > * { position: relative; z-index: 1; }
  .service-icon {
    width: 48px; height: 48px;
    border-radius: 14px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.4rem;
    margin-bottom: 20px;
    background: linear-gradient(135deg, rgba(10,77,255,0.2), rgba(108,78,255,0.2));
  }
  .service-card h3 {
    font-size: 1.1rem;
    font-weight: 700;
    color: white;
    margin-bottom: 8px;
  }
  .service-card p {
    color: rgba(255,255,255,0.5);
    font-size: 0.9rem;
    line-height: 1.6;
  }

  .why-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 24px;
  }
  .why-card {
    background: white;
    border-radius: var(--radius-md);
    padding: 32px;
    box-shadow: var(--shadow-sm);
    border: 1px solid rgba(0,0,0,0.04);
    transition: all 0.4s ease;
    position: relative;
    overflow: hidden;
  }
  .why-card::after {
    content: '';
    position: absolute;
    bottom: 0; left: 0;
    width: 0; height: 3px;
    background: linear-gradient(90deg, var(--deep-blue), var(--cyan));
    transition: width 0.4s ease;
  }
  .why-card:hover::after { width: 100%; }
  .why-card:hover {
    transform: translateY(-4px);
    box-shadow: var(--shadow-md);
  }
  .why-icon {
    width: 52px; height: 52px;
    border-radius: 14px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.5rem;
    margin-bottom: 20px;
  }
  .why-card:nth-child(1) .why-icon { background: rgba(10,77,255,0.08); }
  .why-card:nth-child(2) .why-icon { background: rgba(108,78,255,0.08); }
  .why-card:nth-child(3) .why-icon { background: rgba(0,212,255,0.08); }
  .why-card:nth-child(4) .why-icon { background: rgba(10,77,255,0.08); }
  .why-card:nth-child(5) .why-icon { background: rgba(108,78,255,0.08); }
  .why-card:nth-child(6) .why-icon { background: rgba(0,212,255,0.08); }
  .why-card:nth-child(7) .why-icon { background: rgba(10,77,255,0.08); }
  .why-card:nth-child(8) .why-icon { background: rgba(108,78,255,0.08); }
  .why-card h3 {
    font-size: 1.1rem;
    font-weight: 700;
    color: var(--near-black);
    margin-bottom: 8px;
  }
  .why-card p {
    color: var(--medium-gray);
    font-size: 0.9rem;
    line-height: 1.6;
  }

  .how {
    background: linear-gradient(180deg, var(--light-gray) 0%, white 100%);
  }
  .process-flow {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 24px;
    position: relative;
    max-width: 1000px;
    margin: 0 auto;
  }
  .process-flow::before {
    content: '';
    position: absolute;
    top: 40px; left: 80px; right: 80px;
    height: 2px;
    background: linear-gradient(90deg, var(--deep-blue), var(--purple), var(--cyan));
    opacity: 0.2;
    z-index: 0;
  }
  .process-step {
    flex: 1;
    text-align: center;
    position: relative;
    z-index: 1;
  }
  .step-number {
    width: 80px; height: 80px;
    border-radius: 50%;
    background: white;
    border: 2px solid var(--deep-blue);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.5rem;
    font-weight: 800;
    color: var(--deep-blue);
    margin: 0 auto 20px;
    box-shadow: var(--shadow-md);
    transition: all 0.4s ease;
  }
  .process-step:hover .step-number {
    background: linear-gradient(135deg, var(--deep-blue), var(--purple));
    color: white;
    transform: scale(1.1);
    border-color: transparent;
  }
  .process-step h3 {
    font-size: 1.1rem;
    font-weight: 700;
    color: var(--near-black);
    margin-bottom: 8px;
  }
  .process-step p {
    color: var(--medium-gray);
    font-size: 0.9rem;
  }
  .step-arrow {
    position: absolute;
    top: 36px;
    right: -12px;
    color: var(--deep-blue);
    opacity: 0.3;
    font-size: 1.2rem;
  }

  .stats {
    background: var(--near-black);
    position: relative;
    overflow: hidden;
  }
  .stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 40px;
    text-align: center;
  }
  .stat-item {
    position: relative;
  }
  .stat-number {
    font-size: clamp(2.5rem, 5vw, 3.5rem);
    font-weight: 800;
    background: linear-gradient(135deg, var(--deep-blue), var(--cyan));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1;
    margin-bottom: 8px;
  }
  .stat-label {
    color: rgba(255,255,255,0.5);
    font-size: 0.95rem;
    font-weight: 500;
  }

  .testimonials-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
    gap: 28px;
  }
  .testimonial-card {
    background: white;
    border-radius: var(--radius-lg);
    padding: 36px;
    box-shadow: var(--shadow-sm);
    border: 1px solid rgba(0,0,0,0.04);
    transition: all 0.4s ease;
    position: relative;
  }
  .testimonial-card::before {
    content: '"';
    position: absolute;
    top: 20px; right: 28px;
    font-size: 5rem;
    color: rgba(10,77,255,0.06);
    font-family: Georgia, serif;
    line-height: 1;
  }
  .testimonial-card:hover {
    transform: translateY(-6px);
    box-shadow: var(--shadow-lg);
  }
  .testimonial-text {
    font-size: 1rem;
    color: var(--dark-gray);
    line-height: 1.7;
    margin-bottom: 24px;
    font-style: italic;
  }
  .testimonial-author {
    display: flex;
    align-items: center;
    gap: 16px;
  }
  .author-avatar {
    width: 52px; height: 52px;
    border-radius: 50%;
    background: linear-gradient(135deg, var(--deep-blue), var(--purple));
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-weight: 700;
    font-size: 1.1rem;
    flex-shrink: 0;
  }
  .author-info h4 {
    font-size: 1rem;
    font-weight: 700;
    color: var(--near-black);
  }
  .author-info span {
    font-size: 0.85rem;
    color: var(--medium-gray);
  }

  .faq {
    background: var(--light-gray);
  }
  .faq-list {
    max-width: 800px;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    gap: 12px;
  }
  .faq-item {
    background: white;
    border-radius: var(--radius-md);
    overflow: hidden;
    box-shadow: var(--shadow-sm);
    border: 1px solid rgba(0,0,0,0.04);
    transition: all 0.3s ease;
  }
  .faq-item:hover {
    box-shadow: var(--shadow-md);
  }
  .faq-question {
    width: 100%;
    padding: 24px 28px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: none;
    border: none;
    font-size: 1rem;
    font-weight: 600;
    color: var(--near-black);
    cursor: pointer;
    text-align: left;
    transition: color 0.3s;
  }
  .faq-question:hover { color: var(--deep-blue); }
  .faq-icon {
    width: 28px; height: 28px;
    border-radius: 50%;
    background: var(--light-gray);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1rem;
    transition: all 0.3s ease;
    flex-shrink: 0;
    margin-left: 16px;
  }
  .faq-item.active .faq-icon {
    background: var(--deep-blue);
    color: white;
    transform: rotate(45deg);
  }
  .faq-answer {
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.4s ease, padding 0.4s ease;
  }
  .faq-item.active .faq-answer {
    max-height: 300px;
    padding: 0 28px 24px;
  }
  .faq-answer p {
    color: var(--medium-gray);
    line-height: 1.7;
  }

  .final-cta {
    background: var(--near-black);
    position: relative;
    overflow: hidden;
    text-align: center;
  }
  .final-cta .orb-1 { top: -100px; left: -100px; }
  .final-cta .orb-2 { bottom: -100px; right: -100px; }
  .final-cta h2 {
    font-size: clamp(2rem, 4vw, 3rem);
    font-weight: 800;
    color: white;
    margin-bottom: 16px;
    letter-spacing: -0.02em;
  }
  .final-cta p {
    color: rgba(255,255,255,0.5);
    font-size: 1.1rem;
    max-width: 560px;
    margin: 0 auto 40px;
  }
  .final-cta .btn-secondary {
    background: rgba(255,255,255,0.08);
    border-color: rgba(255,255,255,0.15);
  }
  .final-cta .btn-secondary:hover {
    background: rgba(255,255,255,0.15);
  }

  .footer {
    background: #070914;
    color: rgba(255,255,255,0.5);
    padding: 80px 0 32px;
  }
  .footer-grid {
    display: grid;
    grid-template-columns: 2fr 1fr 1fr 1fr 1.5fr;
    gap: 48px;
    margin-bottom: 64px;
  }
  .footer-brand .logo {
    color: white;
    margin-bottom: 16px;
  }
  .footer-brand p {
    font-size: 0.9rem;
    line-height: 1.7;
    margin-bottom: 24px;
  }
  .social-links {
    display: flex;
    gap: 12px;
  }
  .social-links a {
    width: 40px; height: 40px;
    border-radius: 10px;
    background: rgba(255,255,255,0.05);
    display: flex;
    align-items: center;
    justify-content: center;
    color: rgba(255,255,255,0.6);
    text-decoration: none;
    font-size: 1rem;
    transition: all 0.3s;
  }
  .social-links a:hover {
    background: var(--deep-blue);
    color: white;
    transform: translateY(-2px);
  }
  .footer-col h4 {
    color: white;
    font-size: 0.9rem;
    font-weight: 700;
    margin-bottom: 20px;
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }
  .footer-col ul {
    list-style: none;
  }
  .footer-col li {
    margin-bottom: 12px;
  }
  .footer-col a {
    color: rgba(255,255,255,0.5);
    text-decoration: none;
    font-size: 0.9rem;
    transition: color 0.3s;
  }
  .footer-col a:hover { color: var(--cyan); }
  .newsletter-form {
    display: flex;
    gap: 8px;
  }
  .newsletter-form input {
    flex: 1;
    padding: 12px 16px;
    border-radius: var(--radius-sm);
    border: 1px solid rgba(255,255,255,0.1);
    background: rgba(255,255,255,0.05);
    color: white;
    font-size: 0.9rem;
    outline: none;
    transition: border-color 0.3s;
  }
  .newsletter-form input:focus {
    border-color: var(--deep-blue);
  }
  .newsletter-form input::placeholder {
    color: rgba(255,255,255,0.3);
  }
  .newsletter-form button {
    padding: 12px 20px;
    border-radius: var(--radius-sm);
    background: linear-gradient(135deg, var(--deep-blue), var(--purple));
    color: white;
    border: none;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s;
  }
  .newsletter-form button:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 15px rgba(10,77,255,0.3);
  }
  .footer-bottom {
    border-top: 1px solid rgba(255,255,255,0.06);
    padding-top: 32px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 16px;
    font-size: 0.85rem;
  }

  @media (max-width: 1024px) {
    .about-grid { grid-template-columns: 1fr; }
    .footer-grid { grid-template-columns: 1fr 1fr; }
    .process-flow { flex-wrap: wrap; }
    .process-flow::before { display: none; }
    .process-step { flex: 1 1 45%; }
    .step-arrow { display: none; }
  }
  @media (max-width: 768px) {
    .nav-links {
      position: fixed;
      top: 0; right: -100%;
      width: 80%; max-width: 320px;
      height: 100vh;
      background: white;
      flex-direction: column;
      padding: 80px 32px 32px;
      gap: 24px;
      transition: right 0.4s ease;
      box-shadow: -10px 0 40px rgba(0,0,0,0.1);
    }
    .nav-links.active { right: 0; }
    .nav-links a { color: var(--dark-gray) !important; }
    .mobile-toggle { display: block; }
    .nav-cta { width: 100%; text-align: center; justify-content: center; }
    .hero h1 { font-size: 2.2rem; }
    section { padding: 64px 0; }
    .about-mission { grid-template-columns: 1fr; }
    .process-step { flex: 1 1 100%; }
    .footer-grid { grid-template-columns: 1fr; gap: 32px; }
    .footer-bottom { flex-direction: column; text-align: center; }
  }

  .sr-only {
    position: absolute;
    width: 1px; height: 1px;
    padding: 0; margin: -1px;
    overflow: hidden;
    clip: rect(0,0,0,0);
    white-space: nowrap;
    border: 0;
  }
  :focus-visible {
    outline: 2px solid var(--deep-blue);
    outline-offset: 2px;
  }
  @media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
      animation-duration: 0.01ms !important;
      animation-iteration-count: 1 !important;
      transition-duration: 0.01ms !important;
    }
  }
</style>
</head>
<body>

<!-- NAVIGATION -->
<nav class="navbar" id="navbar" role="navigation" aria-label="Main navigation">
  <div class="nav-container">
    <a href="#" class="logo" aria-label="TechNova Home">
      <div class="logo-icon">T</div>
      TechNova
    </a>
    <button class="mobile-toggle" id="mobileToggle" aria-label="Toggle navigation menu" aria-expanded="false">
      <span></span><span></span><span></span>
    </button>
    <ul class="nav-links" id="navLinks">
      <li><a href="#about">About</a></li>
      <li><a href="#products">Products</a></li>
      <li><a href="#services">Services</a></li>
      <li><a href="#why">Why Us</a></li>
      <li><a href="#process">Process</a></li>
      <li><a href="#testimonials">Testimonials</a></li>
      <li><a href="#faq">FAQ</a></li>
      <li><a href="#contact" class="nav-cta">Book a Demo</a></li>
    </ul>
  </div>
</nav>

<!-- HERO -->
<section class="hero" id="home">
  <div class="hero-bg"></div>
  <div class="hero-grid"></div>
  <div class="hero-orb orb-1" aria-hidden="true"></div>
  <div class="hero-orb orb-2" aria-hidden="true"></div>
  <div class="hero-orb orb-3" aria-hidden="true"></div>
  <div class="hero-content">
    <div class="hero-badge">Trusted by 500+ Organizations Worldwide</div>
    <h1>Technology That Helps Your Business <span class="gradient-text">Grow Smarter</span></h1>
    <p class="hero-sub">We build intelligent software solutions that automate processes, improve productivity, and help organizations thrive in the digital age.</p>
    <div class="hero-cta-group">
      <a href="#products" class="btn btn-primary">Explore Our Products <span>→</span></a>
      <a href="#contact" class="btn btn-secondary">Book a Free Demo</a>
    </div>
  </div>
  <div class="hero-scroll" aria-hidden="true">
    <span>Scroll to explore</span>
    <div class="scroll-line"></div>
  </div>
</section>

<!-- TRUSTED BY -->
<section class="trusted">
  <div class="trusted-inner">
    <p class="trusted-label">Trusted by leading organizations</p>
    <div class="logos-grid">
      <span class="logo-placeholder">EduSmart</span>
      <span class="logo-placeholder">Greenfield Corp</span>
      <span class="logo-placeholder">Grace Ministries</span>
      <span class="logo-placeholder">MetroGov</span>
      <span class="logo-placeholder">NovaStart</span>
      <span class="logo-placeholder">CareFirst NGO</span>
    </div>
  </div>
</section>

<!-- ABOUT -->
<section class="about" id="about">
  <div class="container">
    <div class="section-header animate-on-scroll">
      <span class="section-tag">About Us</span>
      <h2 class="section-title">A Technology Partner You Can Trust</h2>
      <p class="section-desc">More than software — we're your strategic ally in digital transformation.</p>
    </div>
    <div class="about-grid">
      <div class="about-visual animate-on-scroll">
        <div class="glass-card">
          <h3>Building the Future, Together</h3>
          <p>Since our founding, we've partnered with schools, businesses, churches, and government institutions to deliver technology that truly matters.</p>
        </div>
      </div>
      <div class="about-text animate-on-scroll delay-1">
        <h3>Who We Are</h3>
        <p>TechNova is a technology company committed to building intelligent software solutions that solve real-world problems. We don't just write code — we architect systems that transform how organizations operate, compete, and grow.</p>
        <h3>Our Mission</h3>
        <p>To empower every organization with accessible, powerful technology that drives measurable impact and sustainable growth.</p>
        <div class="about-mission">
          <div class="mission-card">
            <div class="icon">🎯</div>
            <h4>Vision</h4>
            <p style="font-size:0.85rem; color:var(--medium-gray);">A world where every organization thrives through technology.</p>
          </div>
          <div class="mission-card">
            <div class="icon">💡</div>
            <h4>Innovation</h4>
            <p style="font-size:0.85rem; color:var(--medium-gray);">Pushing boundaries with AI, cloud, and automation.</p>
          </div>
          <div class="mission-card">
            <div class="icon">🤝</div>
            <h4>Partnership</h4>
            <p style="font-size:0.85rem; color:var(--medium-gray);">Your success is our success. We grow together.</p>
          </div>
          <div class="mission-card">
            <div class="icon">🔒</div>
            <h4>Trust</h4>
            <p style="font-size:0.85rem; color:var(--medium-gray);">Security and reliability in everything we build.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- PRODUCTS -->
<section id="products">
  <div class="container">
    <div class="section-header animate-on-scroll">
      <span class="section-tag">Our Products</span>
      <h2 class="section-title">Software Built for Real Impact</h2>
      <p class="section-desc">Powerful, intuitive solutions designed for the way modern organizations actually work.</p>
    </div>
    <div class="products-grid">
      <div class="product-card animate-on-scroll">
        <div class="product-img">🏫</div>
        <div class="product-info">
          <h3>EduManage Pro</h3>
          <p>Complete school management system with student records, attendance, grading, and parent communication portals.</p>
          <a href="#" class="product-link">Learn More →</a>
        </div>
      </div>
      <div class="product-card animate-on-scroll delay-1">
        <div class="product-img">🏢</div>
        <div class="product-info">
          <h3>BusinessHub</h3>
          <p>All-in-one business operations platform with inventory, HR, finance, and customer management modules.</p>
          <a href="#" class="product-link">Learn More →</a>
        </div>
      </div>
      <div class="product-card animate-on-scroll delay-2">
        <div class="product-img">⛪</div>
        <div class="product-info">
          <h3>ChurchSync</h3>
          <p>Member management, event planning, donation tracking, and sermon distribution for ministries of any size.</p>
          <a href="#" class="product-link">Learn More →</a>
        </div>
      </div>
      <div class="product-card animate-on-scroll delay-3">
        <div class="product-img">📱</div>
        <div class="product-info">
          <h3>MobileFirst Suite</h3>
          <p>Cross-platform mobile applications with offline capabilities, push notifications, and real-time sync.</p>
          <a href="#" class="product-link">Learn More →</a>
        </div>
      </div>
      <div class="product-card animate-on-scroll">
        <div class="product-img">☁️</div>
        <div class="product-info">
          <h3>CloudSync Enterprise</h3>
          <p>Secure cloud infrastructure with automated backups, disaster recovery, and enterprise-grade compliance.</p>
          <a href="#" class="product-link">Learn More →</a>
        </div>
      </div>
      <div class="product-card animate-on-scroll delay-1">
        <div class="product-img">🤖</div>
        <div class="product-info">
          <h3>AI Assist</h3>
          <p>Intelligent automation tools powered by machine learning for customer support, analytics, and forecasting.</p>
          <a href="#" class="product-link">Learn More →</a>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- SERVICES -->
<section class="services" id="services">
  <div class="hero-orb orb-1" style="width:300px;height:300px;top:20%;left:-5%;" aria-hidden="true"></div>
  <div class="hero-orb orb-2" style="width:250px;height:250px;bottom:10%;right:-5%;" aria-hidden="true"></div>
  <div class="container" style="position:relative;z-index:2;">
    <div class="section-header animate-on-scroll">
      <span class="section-tag">Our Services</span>
      <h2 class="section-title">End-to-End Technology Solutions</h2>
      <p class="section-desc">From concept to deployment and beyond — we handle the technology so you can focus on your mission.</p>
    </div>
    <div class="services-grid">
      <div class="service-card animate-on-scroll">
        <div class="service-icon">💻</div>
        <h3>Custom Software Development</h3>
        <p>Tailor-made applications built to solve your unique challenges with scalable, maintainable architecture.</p>
      </div>
      <div class="service-card animate-on-scroll delay-1">
        <div class="service-icon">🏫</div>
        <h3>School Management Systems</h3>
        <p>Streamline admissions, academics, finances, and communication for educational institutions of all sizes.</p>
      </div>
      <div class="service-card animate-on-scroll delay-2">
        <div class="service-icon">📲</div>
        <h3>Mobile App Development</h3>
        <p>Native and cross-platform apps for iOS and Android with stunning UX and rock-solid performance.</p>
      </div>
      <div class="service-card animate-on-scroll delay-3">
        <div class="service-icon">🌐</div>
        <h3>Website Development</h3>
        <p>High-performance, SEO-optimized websites that convert visitors into customers and build brand authority.</p>
      </div>
      <div class="service-card animate-on-scroll">
        <div class="service-icon">⚙️</div>
        <h3>Business Automation</h3>
        <p>Eliminate repetitive tasks with intelligent workflows that save time, reduce errors, and cut costs.</p>
      </div>
      <div class="service-card animate-on-scroll delay-1">
        <div class="service-icon">🧠</div>
        <h3>AI Integration</h3>
        <p>Leverage artificial intelligence for predictive analytics, natural language processing, and smart automation.</p>
      </div>
      <div class="service-card animate-on-scroll delay-2">
        <div class="service-icon">☁️</div>
        <h3>Cloud Solutions</h3>
        <p>Scalable cloud infrastructure, migration services, and managed cloud environments for modern businesses.</p>
      </div>
      <div class="service-card animate-on-scroll delay-3">
        <div class="service-icon">📊</div>
        <h3>IT Consulting</h3>
        <p>Strategic technology advisory to align your IT investments with business goals and digital transformation.</p>
      </div>
      <div class="service-card animate-on-scroll">
        <div class="service-icon">🛠️</div>
        <h3>Technical Support</h3>
        <p>24/7 support, maintenance, and monitoring to keep your systems running smoothly around the clock.</p>
      </div>
    </div>
  </div>
</section>

<!-- WHY CHOOSE US -->
<section id="why">
  <div class="container">
    <div class="section-header animate-on-scroll">
      <span class="section-tag">Why Choose Us</span>
      <h2 class="section-title">The TechNova Advantage</h2>
      <p class="section-desc">We combine technical excellence with genuine partnership to deliver results that matter.</p>
    </div>
    <div class="why-grid">
      <div class="why-card animate-on-scroll">
        <div class="why-icon">🚀</div>
        <h3>Innovative Solutions</h3>
        <p>We stay ahead of the curve, integrating the latest technologies to give you a competitive edge.</p>
      </div>
      <div class="why-card animate-on-scroll delay-1">
        <div class="why-icon">🛡️</div>
        <h3>Reliable Support</h3>
        <p>Our dedicated team is always available to resolve issues and keep your operations running smoothly.</p>
      </div>
      <div class="why-card animate-on-scroll delay-2">
        <div class="why-icon">🔐</div>
        <h3>Secure Technology</h3>
        <p>Enterprise-grade security protocols protect your data at every layer of our infrastructure.</p>
      </div>
      <div class="why-card animate-on-scroll delay-3">
        <div class="why-icon">✨</div>
        <h3>User-Friendly Design</h3>
        <p>Beautiful, intuitive interfaces that your team will actually enjoy using every day.</p>
      </div>
      <div class="why-card animate-on-scroll">
        <div class="why-icon">⚡</div>
        <h3>Fast Deployment</h3>
        <p>Agile methodologies and proven frameworks mean you see results in weeks, not months.</p>
      </div>
      <div class="why-card animate-on-scroll delay-1">
        <div class="why-icon">💰</div>
        <h3>Affordable Pricing</h3>
        <p>Transparent, flexible pricing models that deliver enterprise value without enterprise budgets.</p>
      </div>
      <div class="why-card animate-on-scroll delay-2">
        <div class="why-icon">📈</div>
        <h3>Scalable Systems</h3>
        <p>Architecture designed to grow with you, from startup to enterprise without rebuilding.</p>
      </div>
      <div class="why-card animate-on-scroll delay-3">
        <div class="why-icon">👥</div>
        <h3>Experienced Team</h3>
        <p>Decades of combined experience across industries, technologies, and business challenges.</p>
      </div>
    </div>
  </div>
</section>

<!-- HOW WE WORK -->
<section class="how" id="process">
  <div class="container">
    <div class="section-header animate-on-scroll">
      <span class="section-tag">How We Work</span>
      <h2 class="section-title">A Proven Process for Success</h2>
      <p class="section-desc">Four simple steps from idea to impact.</p>
    </div>
    <div class="process-flow">
      <div class="process-step animate-on-scroll">
        <div class="step-number">1</div>
        <h3>Discover</h3>
        <p>We listen, research, and understand your unique challenges, goals, and constraints.</p>
        <div class="step-arrow">→</div>
      </div>
      <div class="process-step animate-on-scroll delay-1">
        <div class="step-number">2</div>
        <h3>Plan</h3>
        <p>We design a tailored roadmap with clear milestones, deliverables, and success metrics.</p>
        <div class="step-arrow">→</div>
      </div>
      <div class="process-step animate-on-scroll delay-2">
        <div class="step-number">3</div>
        <h3>Build</h3>
        <p>Our engineers bring the vision to life with clean code, rigorous testing, and continuous feedback.</p>
        <div class="step-arrow">→</div>
      </div>
      <div class="process-step animate-on-scroll delay-3">
        <div class="step-number">4</div>
        <h3>Support</h3>
        <p>We stay by your side with training, maintenance, and ongoing optimization.</p>
      </div>
    </div>
  </div>
</section>

<!-- STATS -->
<section class="stats">
  <div class="hero-orb orb-1" style="width:400px;height:400px;top:-100px;left:-100px;" aria-hidden="true"></div>
  <div class="hero-orb orb-2" style="width:350px;height:350px;bottom:-100px;right:-100px;" aria-hidden="true"></div>
  <div class="container" style="position:relative;z-index:2;">
    <div class="stats-grid">
      <div class="stat-item animate-on-scroll">
        <div class="stat-number" data-target="500">0</div>
        <div class="stat-label">Projects Completed</div>
      </div>
      <div class="stat-item animate-on-scroll delay-1">
        <div class="stat-number" data-target="350">0</div>
        <div class="stat-label">Happy Clients</div>
      </div>
      <div class="stat-item animate-on-scroll delay-2">
        <div class="stat-number" data-target="12">0</div>
        <div class="stat-label">Countries Served</div>
      </div>
      <div class="stat-item animate-on-scroll delay-3">
        <div class="stat-number" data-target="8">0</div>
        <div class="stat-label">Years of Experience</div>
      </div>
      <div class="stat-item animate-on-scroll">
        <div class="stat-number" data-target="98">0</div>
        <div class="stat-label">% Customer Satisfaction</div>
      </div>
    </div>
  </div>
</section>

<!-- TESTIMONIALS -->
<section id="testimonials">
  <div class="container">
    <div class="section-header animate-on-scroll">
      <span class="section-tag">Testimonials</span>
      <h2 class="section-title">What Our Clients Say</h2>
      <p class="section-desc">Real stories from organizations we've helped transform.</p>
    </div>
    <div class="testimonials-grid">
      <div class="testimonial-card animate-on-scroll">
        <p class="testimonial-text">TechNova transformed how we manage our entire school. From admissions to grading to parent communication — everything is seamless now. Our staff saves 15+ hours every week.</p>
        <div class="testimonial-author">
          <div class="author-avatar">JD</div>
          <div class="author-info">
            <h4>Dr. James Davidson</h4>
            <span>Principal, EduSmart Academy</span>
          </div>
        </div>
      </div>
      <div class="testimonial-card animate-on-scroll delay-1">
        <p class="testimonial-text">The business automation solution they built for us paid for itself in three months. Our order processing time dropped by 70%. I wish we'd found TechNova sooner.</p>
        <div class="testimonial-author">
          <div class="author-avatar">SO</div>
          <div class="author-info">
            <h4>Sarah Okafor</h4>
            <span>CEO, Greenfield Corp</span>
          </div>
        </div>
      </div>
      <div class="testimonial-card animate-on-scroll delay-2">
        <p class="testimonial-text">Our ministry needed a reliable way to connect with members and manage donations. TechNova delivered a beautiful, easy-to-use platform that our entire congregation loves.</p>
        <div class="testimonial-author">
          <div class="author-avatar">RP</div>
          <div class="author-info">
            <h4>Rev. Peter Adeyemi</h4>
            <span>Lead Pastor, Grace Ministries</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- FAQ -->
<section class="faq" id="faq">
  <div class="container">
    <div class="section-header animate-on-scroll">
      <span class="section-tag">FAQ</span>
      <h2 class="section-title">Frequently Asked Questions</h2>
      <p class="section-desc">Everything you need to know before getting started.</p>
    </div>
    <div class="faq-list">
      <div class="faq-item animate-on-scroll">
        <button class="faq-question" aria-expanded="false">
          How much do your services cost?
          <span class="faq-icon">+</span>
        </button>
        <div class="faq-answer">
          <p>We offer flexible pricing tailored to your project scope and budget. From affordable starter packages for small businesses to comprehensive enterprise solutions, we ensure transparent pricing with no hidden fees. Contact us for a free quote.</p>
        </div>
      </div>
      <div class="faq-item animate-on-scroll delay-1">
        <button class="faq-question" aria-expanded="false">
          What kind of support do you provide?
          <span class="faq-icon">+</span>
        </button>
        <div class="faq-answer">
          <p>We provide 24/7 technical support, regular maintenance, security updates, and dedicated account managers. Our team is always available via phone, email, WhatsApp, and live chat to ensure your systems run flawlessly.</p>
        </div>
      </div>
      <div class="faq-item animate-on-scroll delay-2">
        <button class="faq-question" aria-expanded="false">
          How long does deployment take?
          <span class="faq-icon">+</span>
        </button>
        <div class="faq-answer">
          <p>Most projects are deployed within 4–8 weeks depending on complexity. We use agile methodologies to deliver working features incrementally, so you see progress from week one. Rush deployments are available for urgent needs.</p>
        </div>
      </div>
      <div class="faq-item animate-on-scroll delay-3">
        <button class="faq-question" aria-expanded="false">
          Can your solutions be customized?
          <span class="faq-icon">+</span>
        </button>
        <div class="faq-answer">
          <p>Absolutely. Every solution we build is tailored to your specific workflows, branding, and requirements. We never force a one-size-fits-all approach — your software should work the way you do.</p>
        </div>
      </div>
      <div class="faq-item animate-on-scroll">
        <button class="faq-question" aria-expanded="false">
          How secure is my data?
          <span class="faq-icon">+</span>
        </button>
        <div class="faq-answer">
          <p>Security is our top priority. We implement end-to-end encryption, regular security audits, role-based access controls, and compliance with industry standards like GDPR and ISO 27001. Your data is always protected.</p>
        </div>
      </div>
      <div class="faq-item animate-on-scroll delay-1">
        <button class="faq-question" aria-expanded="false">
          Do you offer maintenance after launch?
          <span class="faq-icon">+</span>
        </button>
        <div class="faq-answer">
          <p>Yes, we offer comprehensive maintenance packages that include bug fixes, performance optimization, feature updates, and dedicated support channels. We believe in long-term partnerships, not one-off projects.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- FINAL CTA -->
<section class="final-cta" id="contact">
  <div class="hero-orb orb-1" aria-hidden="true"></div>
  <div class="hero-orb orb-2" aria-hidden="true"></div>
  <div class="container" style="position:relative;z-index:2;">
    <div class="section-header animate-on-scroll">
      <h2>Ready to Transform Your Organization with Technology?</h2>
      <p>Join hundreds of organizations that have already chosen TechNova as their technology partner. Let's build something extraordinary together.</p>
      <div class="hero-cta-group" style
      with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_code)

print("HTML file created successfully!")