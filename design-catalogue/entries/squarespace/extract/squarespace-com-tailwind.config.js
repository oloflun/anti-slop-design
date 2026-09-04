/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(6, 83%, 97%)',
            '100': 'hsl(6, 83%, 94%)',
            '200': 'hsl(6, 83%, 86%)',
            '300': 'hsl(6, 83%, 76%)',
            '400': 'hsl(6, 83%, 64%)',
            '500': 'hsl(6, 83%, 50%)',
            '600': 'hsl(6, 83%, 40%)',
            '700': 'hsl(6, 83%, 32%)',
            '800': 'hsl(6, 83%, 24%)',
            '900': 'hsl(6, 83%, 16%)',
            '950': 'hsl(6, 83%, 10%)',
            DEFAULT: '#200603'
        },
        secondary: {
            '50': 'hsl(166, 43%, 97%)',
            '100': 'hsl(166, 43%, 94%)',
            '200': 'hsl(166, 43%, 86%)',
            '300': 'hsl(166, 43%, 76%)',
            '400': 'hsl(166, 43%, 64%)',
            '500': 'hsl(166, 43%, 50%)',
            '600': 'hsl(166, 43%, 40%)',
            '700': 'hsl(166, 43%, 32%)',
            '800': 'hsl(166, 43%, 24%)',
            '900': 'hsl(166, 43%, 16%)',
            '950': 'hsl(166, 43%, 10%)',
            DEFAULT: '#1e4c41'
        },
        'neutral-50': '#000000',
        'neutral-100': '#ffffff',
        'neutral-200': '#898989',
        'neutral-300': '#222222',
        'neutral-400': '#2f2f2f',
        'neutral-500': '#0e0e0e',
        'neutral-600': '#e7e7e7',
        'neutral-700': '#dddddd',
        'neutral-800': '#5a5a5a',
        'neutral-900': '#f5f5f4',
        background: '#ffffff',
        foreground: '#000000'
    },
    fontFamily: {
        sans: [
            'Clarkson',
            'sans-serif'
        ],
        heading: [
            'Clarkson Serif',
            'sans-serif'
        ],
        body: [
            'ClarksonLight',
            'sans-serif'
        ]
    },
    fontSize: {
        '12': [
            '12px',
            {
                lineHeight: '16.8px'
            }
        ],
        '13': [
            '13px',
            {
                lineHeight: '18.2px'
            }
        ],
        '14': [
            '14px',
            {
                lineHeight: '14px'
            }
        ],
        '15': [
            '15px',
            {
                lineHeight: '21px',
                letterSpacing: '-0.015px'
            }
        ],
        '16': [
            '16px',
            {
                lineHeight: 'normal'
            }
        ],
        '20': [
            '20px',
            {
                lineHeight: '24px',
                letterSpacing: '-0.2px'
            }
        ],
        '26': [
            '26px',
            {
                lineHeight: '28.08px',
                letterSpacing: '-0.52px'
            }
        ],
        '36': [
            '36px',
            {
                lineHeight: '38.88px',
                letterSpacing: '-1.44px'
            }
        ],
        '50': [
            '50px',
            {
                lineHeight: '54px',
                letterSpacing: '-2px'
            }
        ],
        '60': [
            '60px',
            {
                lineHeight: '62.4px',
                letterSpacing: '-3.6px'
            }
        ],
        '70': [
            '70px',
            {
                lineHeight: '72.8px',
                letterSpacing: '-3.5px'
            }
        ]
    },
    spacing: {
        '1': '2px',
        '4': '8px',
        '20': '40px',
        '24': '48px',
        '26': '52px',
        '28': '56px',
        '40': '80px',
        '60': '120px',
        '80': '160px',
        '120': '240px',
        '63px': '63px'
    },
    borderRadius: {
        sm: '3px',
        md: '6px',
        lg: '16px',
        full: '100px'
    },
    boxShadow: {
        sm: 'color(srgb 0 0 0 / 0.2) 0px 0px 0px 2px inset',
        lg: 'rgba(0, 0, 0, 0.1) 0px 8px 16px 0px',
        xl: 'rgba(0, 0, 0, 0.05) 0px 134px 80px 0px, rgba(0, 0, 0, 0.09) 0px 60px 60px 0px, rgba(0, 0, 0, 0.1) 0px 15px 33px 0px'
    },
    screens: {
        sm: '421px'
    },
    transitionDuration: {
        '100': '0.1s',
        '150': '0.15s',
        '200': '0.2s',
        '250': '0.25s',
        '300': '0.3s',
        '350': '0.35s',
        '450': '0.45s',
        '500': '0.5s',
        '600': '0.6s',
        '700': '0.7s',
        '750': '0.75s',
        '800': '0.8s',
        '1000': '1s'
    },
    transitionTimingFunction: {
        custom: 'cubic-bezier(0.25, 0.46, 0.45, 0.94)',
        linear: 'linear'
    },
    container: {
        center: true,
        padding: '0px'
    },
    maxWidth: {
        container: '2400px'
    }
},
  },
};
