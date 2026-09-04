/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(7, 81%, 97%)',
            '100': 'hsl(7, 81%, 94%)',
            '200': 'hsl(7, 81%, 86%)',
            '300': 'hsl(7, 81%, 76%)',
            '400': 'hsl(7, 81%, 64%)',
            '500': 'hsl(7, 81%, 50%)',
            '600': 'hsl(7, 81%, 40%)',
            '700': 'hsl(7, 81%, 32%)',
            '800': 'hsl(7, 81%, 24%)',
            '900': 'hsl(7, 81%, 16%)',
            '950': 'hsl(7, 81%, 10%)',
            DEFAULT: '#e7371e'
        },
        secondary: {
            '50': 'hsl(335, 70%, 97%)',
            '100': 'hsl(335, 70%, 94%)',
            '200': 'hsl(335, 70%, 86%)',
            '300': 'hsl(335, 70%, 76%)',
            '400': 'hsl(335, 70%, 64%)',
            '500': 'hsl(335, 70%, 50%)',
            '600': 'hsl(335, 70%, 40%)',
            '700': 'hsl(335, 70%, 32%)',
            '800': 'hsl(335, 70%, 24%)',
            '900': 'hsl(335, 70%, 16%)',
            '950': 'hsl(335, 70%, 10%)',
            DEFAULT: '#671235'
        },
        'neutral-50': '#000000',
        'neutral-100': '#ffffff',
        'neutral-200': '#eeeeee',
        background: '#ffffff',
        foreground: '#000000'
    },
    fontFamily: {
        body: [
            'Macan',
            'sans-serif'
        ]
    },
    fontSize: {
        '14': [
            '14px',
            {
                lineHeight: 'normal'
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
                lineHeight: 'normal'
            }
        ],
        '38': [
            '38px',
            {
                lineHeight: '41.8px'
            }
        ],
        '100': [
            '100px',
            {
                lineHeight: '100px',
                letterSpacing: '-2px'
            }
        ]
    },
    spacing: {
        '1': '5px',
        '20': '100px',
        '33': '165px',
        '60': '300px'
    },
    transitionDuration: {
        '200': '0.2s',
        '250': '0.25s',
        '300': '0.3s',
        '350': '0.35s',
        '400': '0.4s',
        '500': '0.5s',
        '650': '0.65s',
        '700': '0.7s',
        '750': '0.75s',
        '1000': '1s',
        '1250': '1.25s'
    },
    transitionTimingFunction: {
        linear: 'linear'
    },
    container: {
        center: true,
        padding: '0px'
    },
    maxWidth: {
        container: '1920px'
    }
},
  },
};
