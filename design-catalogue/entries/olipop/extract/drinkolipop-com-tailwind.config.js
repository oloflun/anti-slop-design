/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(167, 92%, 97%)',
            '100': 'hsl(167, 92%, 94%)',
            '200': 'hsl(167, 92%, 86%)',
            '300': 'hsl(167, 92%, 76%)',
            '400': 'hsl(167, 92%, 64%)',
            '500': 'hsl(167, 92%, 50%)',
            '600': 'hsl(167, 92%, 40%)',
            '700': 'hsl(167, 92%, 32%)',
            '800': 'hsl(167, 92%, 24%)',
            '900': 'hsl(167, 92%, 16%)',
            '950': 'hsl(167, 92%, 10%)',
            DEFAULT: '#034638'
        },
        secondary: {
            '50': 'hsl(60, 100%, 97%)',
            '100': 'hsl(60, 100%, 94%)',
            '200': 'hsl(60, 100%, 86%)',
            '300': 'hsl(60, 100%, 76%)',
            '400': 'hsl(60, 100%, 64%)',
            '500': 'hsl(60, 100%, 50%)',
            '600': 'hsl(60, 100%, 40%)',
            '700': 'hsl(60, 100%, 32%)',
            '800': 'hsl(60, 100%, 24%)',
            '900': 'hsl(60, 100%, 16%)',
            '950': 'hsl(60, 100%, 10%)',
            DEFAULT: '#ffff7d'
        },
        accent: {
            '50': 'hsl(155, 55%, 97%)',
            '100': 'hsl(155, 55%, 94%)',
            '200': 'hsl(155, 55%, 86%)',
            '300': 'hsl(155, 55%, 76%)',
            '400': 'hsl(155, 55%, 64%)',
            '500': 'hsl(155, 55%, 50%)',
            '600': 'hsl(155, 55%, 40%)',
            '700': 'hsl(155, 55%, 32%)',
            '800': 'hsl(155, 55%, 24%)',
            '900': 'hsl(155, 55%, 16%)',
            '950': 'hsl(155, 55%, 10%)',
            DEFAULT: '#98e1c3'
        },
        'neutral-50': '#3a3a3a',
        'neutral-100': '#000000',
        'neutral-200': '#ffffff',
        'neutral-300': '#fff6ea',
        'neutral-400': '#9a9a9a',
        'neutral-500': '#737373',
        'neutral-600': '#4f7456',
        'neutral-700': '#cccccc',
        'neutral-800': '#e3e3e3',
        'neutral-900': '#f0f0f0',
        background: '#ffffff',
        foreground: '#000000'
    },
    fontFamily: {
        sans: [
            'Ano',
            'sans-serif'
        ],
        body: [
            'SF-Secondary-Font',
            'sans-serif'
        ],
        font4: [
            'WindsorEF',
            'sans-serif'
        ]
    },
    fontSize: {
        '10': [
            '10px',
            {
                lineHeight: '10px'
            }
        ],
        '12': [
            '12px',
            {
                lineHeight: '14.4px'
            }
        ],
        '14': [
            '14px',
            {
                lineHeight: '25.2px'
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
                lineHeight: '30px'
            }
        ],
        '20': [
            '20px',
            {
                lineHeight: '20px'
            }
        ],
        '22': [
            '22px',
            {
                lineHeight: '36px'
            }
        ],
        '24': [
            '24px',
            {
                lineHeight: '26.4px'
            }
        ],
        '32': [
            '32px',
            {
                lineHeight: '35.2px'
            }
        ],
        '40': [
            '40px',
            {
                lineHeight: '44px'
            }
        ],
        '48': [
            '48px',
            {
                lineHeight: '62px'
            }
        ],
        '50': [
            '50px',
            {
                lineHeight: '62px'
            }
        ],
        '52': [
            '52px',
            {
                lineHeight: '52px'
            }
        ],
        '54': [
            '54px',
            {
                lineHeight: '54px'
            }
        ],
        '80': [
            '80px',
            {
                lineHeight: '80px'
            }
        ]
    },
    spacing: {
        '0': '0px',
        '15': '30px',
        '18': '36px',
        '20': '40px',
        '24': '48px',
        '30': '60px',
        '36': '72px',
        '40': '80px',
        '43': '86px',
        '46': '92px',
        '53': '106px',
        '60': '120px',
        '80': '160px',
        '84': '168px',
        '86': '172px',
        '112': '224px',
        '124': '248px',
        '45px': '45px',
        '53px': '53px',
        '63px': '63px',
        '263px': '263px',
        '379px': '379px'
    },
    borderRadius: {
        xs: '2px',
        sm: '5px',
        md: '8px',
        lg: '16px',
        xl: '24px',
        full: '9999px'
    },
    boxShadow: {
        sm: 'rgb(20, 67, 61) 0px 0px 0px 1.5px',
        md: 'rgba(0, 0, 0, 0.25) 0px 4px 8px 0px',
        xl: 'rgba(0, 0, 0, 0.12) 0px 0px 80px 0px'
    },
    screens: {
        sm: '650px',
        md: '811px',
        lg: '1024px',
        '1152px': '1152px',
        '1180px': '1180px',
        '1183px': '1183px',
        '1198px': '1198px',
        xl: '1300px',
        '1440px': '1440px',
        '2xl': '1536px',
        '1920px': '1920px'
    },
    transitionDuration: {
        '100': '0.1s',
        '150': '0.15s',
        '200': '0.2s',
        '230': '0.23s',
        '250': '0.25s',
        '300': '0.3s',
        '400': '0.4s',
        '500': '0.5s'
    },
    transitionTimingFunction: {
        default: 'ease',
        custom: 'cubic-bezier(0.18, 0.89, 0.32, 1.28)',
        linear: 'linear'
    },
    container: {
        center: true,
        padding: '2px'
    },
    maxWidth: {
        container: '312px'
    }
},
  },
};
