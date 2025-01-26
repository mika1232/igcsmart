class SiteFooter extends HTMLElement {
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
                :host { /* Target the custom element itself */
                    display: block; /* Make it a block element */
                    width: 100%; /* Take full width */
                    margin-top: auto; /* Push to bottom in flexbox layout */
                }

                footer {
                    text-align: center;
                    padding: 1.5rem 2rem;
                    background-color: rgba(30, 30, 45, 0.9);
                    color: #cccccc;
                }

                footer .social-media a {
                    margin: 0 0.8rem;
                    font-size: 1.2rem;
                    color: #ffffff;
                }

                footer .social-media a:hover {
                    color: #b917e6;
                }

                .beta {
                    padding-bottom: 5px;
                }

                .hr-footer {
                    border-top: 0px;
                    border-left: 0px;
                    border-right: 0px;
                    width: 20%;
                    margin: auto;
                }

                .footer-p {
                    color: #e0dbdb;
                    padding: 5px;
                }
            </style>
            <footer>
                <p class="beta">BETA TESTING 2025</p>
                <hr class="hr-footer">
                <p class="footer-p">The ultimate hub for studying.</p>
                <div class="social-media">
                    <a href="https://www.instagram.com/igcsmart.official/">Instagram</a>
                </div>
            </footer>
        `;
    }
}

customElements.define('site-footer', SiteFooter);