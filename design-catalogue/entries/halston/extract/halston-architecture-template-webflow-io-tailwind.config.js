/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        'neutral-50': '#583939',
        'neutral-100': '#000000',
        'neutral-200': '#ffffff',
        'neutral-300': '#99988f',
        background: '#583939',
        foreground: '#000000'
    },
    fontFamily: {
        sans: [
            'General Sans',
            'sans-serif'
        ],
        body: [
            'JetBrains Mono',
            'sans-serif'
        ]
    },
    fontSize: {
        '16': [
            '16px',
            {
                lineHeight: 'normal'
            }
        ],
        '30': [
            '30px',
            {
                lineHeight: '30px'
            }
        ],
        '56': [
            '56px',
            {
                lineHeight: '56px'
            }
        ],
        '192': [
            '192px',
            {
                lineHeight: '153.6px',
                letterSpacing: '-6.4px'
            }
        ],
        '115.2': [
            '115.2px',
            {
                lineHeight: '92.16px'
            }
        ],
        '102.4': [
            '102.4px',
            {
                lineHeight: '102.4px',
                letterSpacing: '-6.4px'
            }
        ],
        '51.2': [
            '51.2px',
            {
                lineHeight: '51.2px'
            }
        ],
        '40.8': [
            '40.8px',
            {
                lineHeight: '40.8px'
            }
        ],
        '38.4': [
            '38.4px',
            {
                lineHeight: '38.4px'
            }
        ],
        '26.4': [
            '26.4px',
            {
                lineHeight: '26.4px'
            }
        ],
        '25.6': [
            '25.6px',
            {
                lineHeight: '25.6px',
                letterSpacing: '12.8px'
            }
        ],
        '20.4': [
            '20.4px',
            {
                lineHeight: '22.44px'
            }
        ],
        '19.2': [
            '19.2px',
            {
                lineHeight: '19.2px'
            }
        ],
        '17.2': [
            '17.2px',
            {
                lineHeight: '25.8px'
            }
        ],
        '14.6': [
            '14.6px',
            {
                lineHeight: '18.98px',
                letterSpacing: '0.8px'
            }
        ]
    },
    spacing: {
        '21': '42px',
        '24': '48px',
        '32': '64px',
        '40': '80px',
        '48': '96px',
        '96': '192px',
        '160': '320px',
        '3px': '3px',
        '115px': '115px',
        '483px': '483px'
    },
    borderRadius: {
        sm: '3px',
        full: '50px'
    },
    screens: {
        md: '768px'
    },
    transitionDuration: {
        '1': '0.001s',
        '200': '0.2s'
    },
    container: {
        center: true,
        padding: '0px'
    },
    maxWidth: {
        container: '1280px'
    }
},
  },
};
