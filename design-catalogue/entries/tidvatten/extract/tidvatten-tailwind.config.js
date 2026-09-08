/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(7, 100%, 97%)',
            '100': 'hsl(7, 100%, 94%)',
            '200': 'hsl(7, 100%, 86%)',
            '300': 'hsl(7, 100%, 76%)',
            '400': 'hsl(7, 100%, 64%)',
            '500': 'hsl(7, 100%, 50%)',
            '600': 'hsl(7, 100%, 40%)',
            '700': 'hsl(7, 100%, 32%)',
            '800': 'hsl(7, 100%, 24%)',
            '900': 'hsl(7, 100%, 16%)',
            '950': 'hsl(7, 100%, 10%)',
            DEFAULT: '#680c00'
        },
        secondary: {
            '50': 'hsl(12, 89%, 97%)',
            '100': 'hsl(12, 89%, 94%)',
            '200': 'hsl(12, 89%, 86%)',
            '300': 'hsl(12, 89%, 76%)',
            '400': 'hsl(12, 89%, 64%)',
            '500': 'hsl(12, 89%, 50%)',
            '600': 'hsl(12, 89%, 40%)',
            '700': 'hsl(12, 89%, 32%)',
            '800': 'hsl(12, 89%, 24%)',
            '900': 'hsl(12, 89%, 16%)',
            '950': 'hsl(12, 89%, 10%)',
            DEFAULT: '#af2c0a'
        },
        'neutral-50': '#e5e7eb',
        'neutral-100': '#020304',
        'neutral-200': '#d6e0e5',
        'neutral-300': '#12161b',
        'neutral-400': '#6d7c85',
        'neutral-500': '#cbd6de',
        'neutral-600': '#b1c0ca',
        background: '#cbd6de',
        foreground: '#020304'
    },
    fontFamily: {
        body: [
            'Fragment Mono',
            'sans-serif'
        ],
        font2: [
            'Familjen Grotesk',
            'sans-serif'
        ]
    },
    fontSize: {
        '64': [
            '64px',
            {
                lineHeight: '60.8px',
                letterSpacing: '-1.28px'
            }
        ],
        '166.4': [
            '166.4px',
            {
                lineHeight: '166.4px',
                letterSpacing: '-3.328px'
            }
        ],
        '147.2': [
            '147.2px',
            {
                lineHeight: '132.48px',
                letterSpacing: '-2.944px'
            }
        ],
        '76.8': [
            '76.8px',
            {
                lineHeight: '69.12px',
                letterSpacing: '-1.536px'
            }
        ],
        '46.08': [
            '46.08px',
            {
                lineHeight: '46.08px',
                letterSpacing: '-0.9216px'
            }
        ],
        '43.52': [
            '43.52px',
            {
                lineHeight: '41.344px',
                letterSpacing: '-0.8704px'
            }
        ],
        '35.84': [
            '35.84px',
            {
                lineHeight: '35.84px'
            }
        ],
        '34.56': [
            '34.56px',
            {
                lineHeight: '51.84px',
                letterSpacing: '-0.3456px'
            }
        ],
        '30.72': [
            '30.72px',
            {
                lineHeight: '30.72px'
            }
        ],
        '25.6': [
            '25.6px',
            {
                lineHeight: '35.2px',
                letterSpacing: '0.512px'
            }
        ],
        '23.04': [
            '23.04px',
            {
                lineHeight: '31.104px',
                letterSpacing: '0.4608px'
            }
        ],
        '22.5': [
            '22.5px',
            {
                lineHeight: '31.5px',
                letterSpacing: '3.15px'
            }
        ],
        '21.6': [
            '21.6px',
            {
                lineHeight: '33.48px'
            }
        ],
        '20.7': [
            '20.7px',
            {
                lineHeight: '33.12px'
            }
        ],
        '20.25': [
            '20.25px',
            {
                lineHeight: '31.5px'
            }
        ]
    },
    spacing: {
        '36': '72px',
        '45': '90px',
        '54': '108px',
        '81': '162px',
        '90': '180px',
        '99': '198px',
        '5px': '5px',
        '45px': '45px',
        '63px': '63px'
    },
    screens: {
        md: '768px',
        lg: '1024px'
    },
    transitionDuration: {
        '150': '0.15s',
        '500': '0.5s',
        '1250': '1.25s',
        '1400': '1.4s'
    },
    transitionTimingFunction: {
        custom: 'cubic-bezier(0.16, 1, 0.3, 1)'
    },
    container: {
        center: true,
        padding: '63px'
    },
    maxWidth: {
        container: '1680px'
    }
},
  },
};
