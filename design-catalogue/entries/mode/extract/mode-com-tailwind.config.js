/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(78, 83%, 97%)',
            '100': 'hsl(78, 83%, 94%)',
            '200': 'hsl(78, 83%, 86%)',
            '300': 'hsl(78, 83%, 76%)',
            '400': 'hsl(78, 83%, 64%)',
            '500': 'hsl(78, 83%, 50%)',
            '600': 'hsl(78, 83%, 40%)',
            '700': 'hsl(78, 83%, 32%)',
            '800': 'hsl(78, 83%, 24%)',
            '900': 'hsl(78, 83%, 16%)',
            '950': 'hsl(78, 83%, 10%)',
            DEFAULT: '#c8f169'
        },
        secondary: {
            '50': 'hsl(163, 88%, 97%)',
            '100': 'hsl(163, 88%, 94%)',
            '200': 'hsl(163, 88%, 86%)',
            '300': 'hsl(163, 88%, 76%)',
            '400': 'hsl(163, 88%, 64%)',
            '500': 'hsl(163, 88%, 50%)',
            '600': 'hsl(163, 88%, 40%)',
            '700': 'hsl(163, 88%, 32%)',
            '800': 'hsl(163, 88%, 24%)',
            '900': 'hsl(163, 88%, 16%)',
            '950': 'hsl(163, 88%, 10%)',
            DEFAULT: '#043f2e'
        },
        accent: {
            '50': 'hsl(217, 80%, 97%)',
            '100': 'hsl(217, 80%, 94%)',
            '200': 'hsl(217, 80%, 86%)',
            '300': 'hsl(217, 80%, 76%)',
            '400': 'hsl(217, 80%, 64%)',
            '500': 'hsl(217, 80%, 50%)',
            '600': 'hsl(217, 80%, 40%)',
            '700': 'hsl(217, 80%, 32%)',
            '800': 'hsl(217, 80%, 24%)',
            '900': 'hsl(217, 80%, 16%)',
            '950': 'hsl(217, 80%, 10%)',
            DEFAULT: '#1863dc'
        },
        'neutral-50': '#000000',
        'neutral-100': '#212121',
        'neutral-200': '#fcfcfc',
        'neutral-300': '#f4f4f4',
        'neutral-400': '#d0d5d2',
        background: '#ffffff',
        foreground: '#000000'
    },
    fontFamily: {
        body: [
            '--fonts-sans',
            'sans-serif'
        ],
        heading: [
            'Grenette',
            'sans-serif'
        ]
    },
    fontSize: {
        '12': [
            '12px',
            {
                lineHeight: '24px'
            }
        ],
        '14': [
            '14px',
            {
                lineHeight: '24px'
            }
        ],
        '16': [
            '16px',
            {
                lineHeight: 'normal'
            }
        ],
        '18': [
            '18px',
            {
                lineHeight: '24px'
            }
        ],
        '22': [
            '22px',
            {
                lineHeight: '26.84px',
                letterSpacing: '-3%'
            }
        ],
        '24': [
            '24px',
            {
                lineHeight: '28.8px',
                letterSpacing: '0%'
            }
        ],
        '36': [
            '36px',
            {
                lineHeight: '37.08px',
                letterSpacing: '-0.36px'
            }
        ],
        '56': [
            '56px',
            {
                lineHeight: '67.2px',
                letterSpacing: '-1.12px'
            }
        ],
        '70': [
            '70px',
            {
                lineHeight: '77px',
                letterSpacing: '-2.1px'
            }
        ],
        '72': [
            '72px',
            {
                lineHeight: '79.2px',
                letterSpacing: '-1.44px'
            }
        ],
        '96': [
            '96px',
            {
                lineHeight: '86.4px',
                letterSpacing: '-1.92px'
            }
        ],
        '153.6': [
            '153.6px',
            {
                lineHeight: '153.6px',
                letterSpacing: '-3.072px'
            }
        ]
    },
    spacing: {
        '1': '2px',
        '4': '8px',
        '18': '36px',
        '20': '40px',
        '25': '50px',
        '30': '60px',
        '45': '90px',
        '50': '100px',
        '60': '120px',
        '65': '130px',
        '100': '200px',
        '120': '240px',
        '55px': '55px'
    },
    borderRadius: {
        xs: '2px',
        sm: '5px',
        md: '8px',
        lg: '16px',
        full: '50px'
    },
    boxShadow: {
        md: 'rgba(172, 171, 171, 0.3) 0px -1px 10px 0px',
        xl: 'rgba(0, 0, 0, 0.3) 0px 32px 68px 0px'
    },
    screens: {
        lg: '992px',
        '1200px': '1200px'
    },
    transitionDuration: {
        '150': '0.15s',
        '200': '0.2s',
        '250': '0.25s',
        '350': '0.35s',
        '400': '0.4s',
        '500': '0.5s',
        '1000': '1s'
    },
    transitionTimingFunction: {
        default: 'ease',
        custom: 'cubic-bezier(0.75, 0, 0.29, 1.01)'
    },
    container: {
        center: true,
        padding: '0px'
    },
    maxWidth: {
        container: '100%'
    }
},
  },
};
