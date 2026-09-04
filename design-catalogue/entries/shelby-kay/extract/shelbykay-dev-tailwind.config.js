/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(28, 45%, 97%)',
            '100': 'hsl(28, 45%, 94%)',
            '200': 'hsl(28, 45%, 86%)',
            '300': 'hsl(28, 45%, 76%)',
            '400': 'hsl(28, 45%, 64%)',
            '500': 'hsl(28, 45%, 50%)',
            '600': 'hsl(28, 45%, 40%)',
            '700': 'hsl(28, 45%, 32%)',
            '800': 'hsl(28, 45%, 24%)',
            '900': 'hsl(28, 45%, 16%)',
            '950': 'hsl(28, 45%, 10%)',
            DEFAULT: '#d6b292'
        },
        secondary: {
            '50': 'hsl(35, 41%, 97%)',
            '100': 'hsl(35, 41%, 94%)',
            '200': 'hsl(35, 41%, 86%)',
            '300': 'hsl(35, 41%, 76%)',
            '400': 'hsl(35, 41%, 64%)',
            '500': 'hsl(35, 41%, 50%)',
            '600': 'hsl(35, 41%, 40%)',
            '700': 'hsl(35, 41%, 32%)',
            '800': 'hsl(35, 41%, 24%)',
            '900': 'hsl(35, 41%, 16%)',
            '950': 'hsl(35, 41%, 10%)',
            DEFAULT: '#efe6d9'
        },
        'neutral-50': '#393c2a',
        'neutral-100': '#000000',
        'neutral-200': '#737955',
        'neutral-300': '#afa199',
        'neutral-400': '#7b8785',
        background: '#efe6d9',
        foreground: '#393c2a'
    },
    fontFamily: {
        sans: [
            'Switzer',
            'sans-serif'
        ],
        heading: [
            'Ranade',
            'sans-serif'
        ]
    },
    fontSize: {
        '10': [
            '10px',
            {
                lineHeight: '12px'
            }
        ],
        '11': [
            '11px',
            {
                lineHeight: '11px'
            }
        ],
        '14': [
            '14px',
            {
                lineHeight: '16.8px'
            }
        ],
        '16': [
            '16px',
            {
                lineHeight: '20px'
            }
        ],
        '20': [
            '20px',
            {
                lineHeight: '24px'
            }
        ],
        '24': [
            '24px',
            {
                lineHeight: '28.8px'
            }
        ],
        '256': [
            '256px',
            {
                lineHeight: '230.4px'
            }
        ],
        '140.8': [
            '140.8px',
            {
                lineHeight: '140.8px'
            }
        ],
        '73.92': [
            '73.92px',
            {
                lineHeight: '73.92px'
            }
        ]
    },
    spacing: {
        '3': '6px',
        '28': '56px',
        '40': '80px',
        '56': '112px',
        '64': '128px',
        '100': '200px',
        '124': '248px',
        '35px': '35px'
    },
    transitionDuration: {
        '100': '0.1s',
        '400': '0.4s',
        '500': '0.5s',
        '600': '0.6s',
        '1200': '1.2s',
        '1250': '1.25s'
    },
    transitionTimingFunction: {
        custom: 'cubic-bezier(0.165, 0.84, 0.44, 1)'
    },
    container: {
        center: true,
        padding: '19.2px'
    },
    maxWidth: {
        container: '1800px'
    }
},
  },
};
