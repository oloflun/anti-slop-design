/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(48, 24%, 97%)',
            '100': 'hsl(48, 24%, 94%)',
            '200': 'hsl(48, 24%, 86%)',
            '300': 'hsl(48, 24%, 76%)',
            '400': 'hsl(48, 24%, 64%)',
            '500': 'hsl(48, 24%, 50%)',
            '600': 'hsl(48, 24%, 40%)',
            '700': 'hsl(48, 24%, 32%)',
            '800': 'hsl(48, 24%, 24%)',
            '900': 'hsl(48, 24%, 16%)',
            '950': 'hsl(48, 24%, 10%)',
            DEFAULT: '#f7f6f2'
        },
        secondary: {
            '50': 'hsl(11, 93%, 97%)',
            '100': 'hsl(11, 93%, 94%)',
            '200': 'hsl(11, 93%, 86%)',
            '300': 'hsl(11, 93%, 76%)',
            '400': 'hsl(11, 93%, 64%)',
            '500': 'hsl(11, 93%, 50%)',
            '600': 'hsl(11, 93%, 40%)',
            '700': 'hsl(11, 93%, 32%)',
            '800': 'hsl(11, 93%, 24%)',
            '900': 'hsl(11, 93%, 16%)',
            '950': 'hsl(11, 93%, 10%)',
            DEFAULT: '#f74c25'
        },
        'neutral-50': '#e5e7eb',
        'neutral-100': '#000000',
        'neutral-200': '#12110c',
        'neutral-300': '#525252',
        'neutral-400': '#ffffff',
        'neutral-500': '#cacac3',
        background: '#f7f6f2',
        foreground: '#f74c25'
    },
    fontFamily: {
        sans: [
            '__Inter_f367f3',
            'sans-serif'
        ],
        heading: [
            'Arial',
            'sans-serif'
        ],
        font2: [
            '__p22MackinacPro_6ce25e',
            'sans-serif'
        ],
        font3: [
            'Inter',
            'sans-serif'
        ],
        font4: [
            '__interDisplay_4fc95a',
            'sans-serif'
        ]
    },
    fontSize: {
        '12': [
            '12px',
            {
                lineHeight: '12px'
            }
        ],
        '14': [
            '14px',
            {
                lineHeight: '18.2px'
            }
        ],
        '16': [
            '16px',
            {
                lineHeight: '24px'
            }
        ],
        '18': [
            '18px',
            {
                lineHeight: '19.8px',
                letterSpacing: '-0.0324px'
            }
        ],
        '20': [
            '20px',
            {
                lineHeight: '22px',
                letterSpacing: '-0.08px'
            }
        ],
        '24': [
            '24px',
            {
                lineHeight: '28.8px',
                letterSpacing: '-0.24px'
            }
        ],
        '30': [
            '30px',
            {
                lineHeight: '36px',
                letterSpacing: '-0.3px'
            }
        ],
        '36': [
            '36px',
            {
                lineHeight: '39.6px',
                letterSpacing: '-0.36px'
            }
        ],
        '60': [
            '60px',
            {
                lineHeight: '63.6px',
                letterSpacing: '-1.74px'
            }
        ],
        '82': [
            '82px',
            {
                lineHeight: '65.6px',
                letterSpacing: '-4.1px'
            }
        ]
    },
    spacing: {
        '15': '30px',
        '20': '40px',
        '24': '48px',
        '28': '56px',
        '35': '70px',
        '50': '100px',
        '60': '120px',
        '80': '160px',
        '91': '182px',
        '95': '190px',
        '120': '240px',
        '141': '282px',
        '160': '320px',
        '1px': '1px',
        '195px': '195px'
    },
    borderRadius: {
        md: '8px',
        lg: '16px',
        full: '9999px'
    },
    boxShadow: {
        lg: 'rgba(0, 0, 0, 0.26) 0px 4px 25px 0px'
    },
    screens: {
        md: '800px',
        lg: '1024px',
        '1440px': '1440px'
    },
    transitionDuration: {
        '140': '0.14s',
        '150': '0.15s',
        '180': '0.18s',
        '200': '0.2s',
        '300': '0.3s',
        '500': '0.5s'
    },
    transitionTimingFunction: {
        default: 'ease',
        linear: 'linear'
    },
    container: {
        center: true,
        padding: '0px'
    },
    maxWidth: {
        container: '1960px'
    }
},
  },
};
