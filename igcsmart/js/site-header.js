class SiteHeader extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: 'open' });
  }

  connectedCallback() {
    this.render();
  }

  render() {
    this.shadowRoot.innerHTML = `
      <style>
        header {
          display: flex;
          justify-content: space-between;
          align-items: center;
          padding: 1rem 3rem;
          padding-left: 0px;
          background-color: rgba(30, 30, 45, 0.8);
          box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
          width: 100%;
          height: 80px; /* Set a FIXED height for the header */
        }

        .logo {
          display: flex;
          align-items: center;
        }

        .logo-image {
          padding-left: 0px;
          max-height: 100%;
          max-width: 200px;
          object-fit: contain; /* Key: Ensures image fits within container */
          display: block;
        }

        a {
          color: #ffffff;
          text-decoration: none;
          transition: color 0.3s;
        }

        nav {
          display: flex;
          align-items: center;
          padding-right: 2rem;
        }

        nav a {
          margin-left: 1.5rem;
          font-size: 1.3rem;
          position: relative;
          transition: all 0.3s ease;
        }

        nav a:hover {
          cursor: pointer;
          letter-spacing: 0.05em;
          transition: 0.25s ease-out;
        }
        nav a::after {
            content: "";
            position: absolute;
            bottom: -3px;
            left: 0;
            width: 0;
            height: 2px;
            background-color: #b917e6;
            transition: width 0.3s ease;
        }
        nav a:hover::after {
            width: 100%;
        }

        .logo {
          font-size: 1.8rem;
          font-weight: bold;
          color: #b917e6;
          text-shadow: 0px 0px 8px #b917e6;
        }
      </style>
      <header>
        <div class="logo"><img class="logo-image" src="../img/logo.png" alt="Site Logo"></div>
        <nav>
          <a href="/">Home</a>
          <a href="/html/about.html">About Us</a>
        </nav>
      </header>
    `;
  }
}

customElements.define('site-header', SiteHeader);