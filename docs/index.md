<style>
  /* Reset some default styles */
  body, html {
    margin: 0;
    padding: 0;
    height: 100%;
    width: 100%;
  }
  
  /* Ensure full width content */
  .md-content__inner {
    margin: 0 !important;
    max-width: none !important;
    padding: 0 !important;
  }

  section {
    min-height: 100vh;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 2rem;
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
    box-sizing: border-box;
  }

  .content {
    background-color: rgba(0, 0, 0, 0.7);
    border-radius: 15px;
    padding: 2rem;
    width: 100%;
    max-width: 1200px;
    margin: 0 auto;
    color: white;
  }

  #hero {
    background-image: url('assets/images/alpaca_bg.png');
  }
  #features {
    background-image: url('https://images.unsplash.com/photo-1451187580459-43490279c0fa?ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80');
  }
  #vision {
    background-image: url('https://images.unsplash.com/photo-1535868463750-c78d9543614f?ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80');
  }
  #problem-statement {
    background-image: url('https://images.unsplash.com/photo-1542831371-29b0f74f9713?ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80');
  }

  h1, h2 {
    color: #FFFFFF;
  }

  ul {
    text-align: left;
    margin: auto%;
    padding-left: 40%;
  }

  .cta-buttons {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 1rem;
    margin-top: 1rem;
  }

  .md-button {
    display: inline-block;
    padding: 0.7em 1.5em;
    text-decoration: none;
    background-color: #3498db;
    color: white;
    border-radius: 4px;
    transition: background-color 0.3s;
    font-weight: bold;
  }

  .md-button:hover {
    background-color: #2980b9;
  }

  .md-button--primary {
    background-color: #e74c3c;
  }

  .md-button--primary:hover {
    background-color: #c0392b;
  }

  .feature-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1rem;
    margin-top: 1rem;
  }

  .feature-item {
    background-color: rgba(255, 255, 255, 0.1);
    padding: 1rem;
    border-radius: 10px;
  }

  @media (max-width: 768px) {
    section {
      padding: 1rem;
    }
    .content {
      padding: 1.5rem;
    }
  }
</style>

<section id="hero">
  <div class="content">
    <h2>Welcome to AlpacAI</h2>
    <p>AlpacAI represents a cutting-edge integration of AI technologies with automotive safety systems, designed to redefine the driving experience. Our mission is to make driving safer, more enjoyable, and more intelligent through the power of artificial intelligence.</p>
    <div class="cta-buttons">
      <a href="{{ 'installation/prerequisites/' | url }}" class="md-button md-button--primary">Get Started with Installation</a>
      <a href="{{ 'vision/' | url }}" class="md-button">Learn More About Our Vision</a>
    </div>
  </div>
</section>

<section id="features">
  <div class="content">
    <h2>Key Features</h2>
    <div class="feature-grid">
      <div class="feature-item">
        <h3>Advanced Driver Monitoring</h3>
        <p>Leveraging computer vision to ensure driver attentiveness.</p>
      </div>
      <div class="feature-item">
        <h3>Interactive Assistance</h3>
        <p>Natural language processing for intuitive driver communication.</p>
      </div>
      <div class="feature-item">
        <h3>Predictive Accident Avoidance</h3>
        <p>Machine learning algorithms to anticipate and prevent potential accidents.</p>
      </div>
      <div class="feature-item">
        <h3>Smart City Integration</h3>
        <p>Connecting with urban infrastructure for optimized routing and enhanced safety.</p>
      </div>
    </div>
  </div>
</section>

<section id="vision">
  <div class="content">
    <h2>Our Vision</h2>
    <p>At AlpacAI, we envision a future where driving is not just safer, but also more enjoyable and seamlessly integrated with artificial intelligence. We're driving towards a future where every journey is safe, efficient, and enjoyable, powered by the intelligent fusion of human insight and artificial intelligence.</p>
    <div class="cta-buttons">
      <a href="{{ 'vision/' | url }}" class="md-button md-button--primary">Explore Our Full Vision</a>
    </div>
  </div>
</section>

<section id="problem-statement">
  <div class="content">
    <h2>Problem Statement</h2>
    <p>AlpacAI addresses critical issues in automotive safety:</p>
    <ul>
      <li>Driver distraction and fatigue remain leading causes of road accidents.</li>
      <li>Information overload from multiple vehicle systems can itself become a source of distraction.</li>
      <li>Many current safety systems are reactive rather than proactive.</li>
      <li>There's untapped potential in using AI to create more intelligent, adaptive, and personalized safety systems.</li>
    </ul>
    <div class="cta-buttons">
      <a href="{{ 'problem-statement/' | url }}" class="md-button md-button--primary">Read Full Problem Statement</a>
    </div>
  </div>
</section>