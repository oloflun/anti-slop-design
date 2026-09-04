/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(11, 52%, 97%)',
            '100': 'hsl(11, 52%, 94%)',
            '200': 'hsl(11, 52%, 86%)',
            '300': 'hsl(11, 52%, 76%)',
            '400': 'hsl(11, 52%, 64%)',
            '500': 'hsl(11, 52%, 50%)',
            '600': 'hsl(11, 52%, 40%)',
            '700': 'hsl(11, 52%, 32%)',
            '800': 'hsl(11, 52%, 24%)',
            '900': 'hsl(11, 52%, 16%)',
            '950': 'hsl(11, 52%, 10%)',
            DEFAULT: '#9e4632'
        },
        secondary: {
            '50': 'hsl(12, 63%, 97%)',
            '100': 'hsl(12, 63%, 94%)',
            '200': 'hsl(12, 63%, 86%)',
            '300': 'hsl(12, 63%, 76%)',
            '400': 'hsl(12, 63%, 64%)',
            '500': 'hsl(12, 63%, 50%)',
            '600': 'hsl(12, 63%, 40%)',
            '700': 'hsl(12, 63%, 32%)',
            '800': 'hsl(12, 63%, 24%)',
            '900': 'hsl(12, 63%, 16%)',
            '950': 'hsl(12, 63%, 10%)',
            DEFAULT: '#471b10'
        },
        accent: {
            '50': 'hsl(11, 45%, 97%)',
            '100': 'hsl(11, 45%, 94%)',
            '200': 'hsl(11, 45%, 86%)',
            '300': 'hsl(11, 45%, 76%)',
            '400': 'hsl(11, 45%, 64%)',
            '500': 'hsl(11, 45%, 50%)',
            '600': 'hsl(11, 45%, 40%)',
            '700': 'hsl(11, 45%, 32%)',
            '800': 'hsl(11, 45%, 24%)',
            '900': 'hsl(11, 45%, 16%)',
            '950': 'hsl(11, 45%, 10%)',
            DEFAULT: '#ba5d48'
        },
        'neutral-50': '#f3eeed',
        'neutral-100': '#000000',
        'neutral-200': '#ffffff',
        background: '#2a0800',
        foreground: '#000000'
    },
    fontFamily: {
        body: [
            'Funnel Sans',
            'sans-serif'
        ],
        heading: [
            'Ltremark',
            'sans-serif'
        ],
        font2: [
            'Funnel Display',
            'sans-serif'
        ]
    },
    fontSize: {
        '48': [
            '48px',
            {
                lineHeight: '57.6px'
            }
        ],
        '56': [
            '56px',
            {
                lineHeight: '67.2px'
            }
        ],
        '64': [
            '64px',
            {
                lineHeight: '76.8px'
            }
        ],
        '96': [
            '96px',
            {
                lineHeight: '96px'
            }
        ],
        '128': [
            '128px',
            {
                lineHeight: '128px'
            }
        ],
        '217.6': [
            '217.6px',
            {
                lineHeight: '261.12px',
                letterSpacing: '-6.4px'
            }
        ],
        '115.2': [
            '115.2px',
            {
                lineHeight: '115.2px'
            }
        ],
        '76.8': [
            '76.8px',
            {
                lineHeight: '84.48px'
            }
        ],
        '54.4': [
            '54.4px',
            {
                lineHeight: '65.28px'
            }
        ],
        '51.2': [
            '51.2px',
            {
                lineHeight: '56.32px'
            }
        ],
        '36.8': [
            '36.8px',
            {
                lineHeight: '44.16px'
            }
        ],
        '30.4': [
            '30.4px',
            {
                lineHeight: '28.8px'
            }
        ],
        '22.4': [
            '22.4px',
            {
                lineHeight: '33.6px'
            }
        ],
        '20.8': [
            '20.8px',
            {
                lineHeight: '24.96px'
            }
        ],
        '19.2': [
            '19.2px',
            {
                lineHeight: '28.8px'
            }
        ]
    },
    spacing: {
        '16': '32px',
        '19': '38px',
        '24': '48px',
        '45': '90px',
        '51': '102px',
        '56': '112px',
        '64': '128px',
        '68': '136px',
        '80': '160px',
        '120': '240px',
        '160': '320px',
        '224': '448px',
        '1px': '1px',
        '77px': '77px'
    },
    borderRadius: {
        md: '10px',
        lg: '14px',
        xl: '20px',
        full: '999px'
    },
    screens: {
        md: '768px'
    },
    transitionDuration: {
        '1': '0.001s',
        '100': '0.1s',
        '200': '0.2s',
        '600': '0.6s',
        '1000': '1s',
        '1200': '1.2s'
    },
    transitionTimingFunction: {
        custom: 'cubic-bezier(0.075, 0.82, 0.165, 1)'
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
