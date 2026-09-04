/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(9, 100%, 97%)',
            '100': 'hsl(9, 100%, 94%)',
            '200': 'hsl(9, 100%, 86%)',
            '300': 'hsl(9, 100%, 76%)',
            '400': 'hsl(9, 100%, 64%)',
            '500': 'hsl(9, 100%, 50%)',
            '600': 'hsl(9, 100%, 40%)',
            '700': 'hsl(9, 100%, 32%)',
            '800': 'hsl(9, 100%, 24%)',
            '900': 'hsl(9, 100%, 16%)',
            '950': 'hsl(9, 100%, 10%)',
            DEFAULT: '#ff6347'
        },
        secondary: {
            '50': 'hsl(32, 43%, 97%)',
            '100': 'hsl(32, 43%, 94%)',
            '200': 'hsl(32, 43%, 86%)',
            '300': 'hsl(32, 43%, 76%)',
            '400': 'hsl(32, 43%, 64%)',
            '500': 'hsl(32, 43%, 50%)',
            '600': 'hsl(32, 43%, 40%)',
            '700': 'hsl(32, 43%, 32%)',
            '800': 'hsl(32, 43%, 24%)',
            '900': 'hsl(32, 43%, 16%)',
            '950': 'hsl(32, 43%, 10%)',
            DEFAULT: '#eee2d4'
        },
        'neutral-50': '#000000',
        'neutral-100': '#ffffff',
        'neutral-200': '#f0f0f0',
        'neutral-300': '#1a1a1a',
        background: '#ffffff',
        foreground: '#000000'
    },
    fontFamily: {
        sans: [
            'Recife',
            'sans-serif'
        ],
        body: [
            'Arial',
            'sans-serif'
        ],
        font2: [
            'Icons',
            'sans-serif'
        ]
    },
    fontSize: {
        '28': [
            '28px',
            {
                lineHeight: '28px'
            }
        ],
        '28.8': [
            '28.8px',
            {
                lineHeight: '28.8px'
            }
        ],
        '23.04': [
            '23.04px',
            {
                lineHeight: '23.04px'
            }
        ],
        '13.3333': [
            '13.3333px',
            {
                lineHeight: 'normal'
            }
        ],
        '11.52': [
            '11.52px',
            {
                lineHeight: 'normal'
            }
        ]
    },
    spacing: {
        '0': '1px',
        '1': '58px',
        '2': '99px',
        '3': '116px',
        '4': '143px',
        '5': '269px',
        '6': '293px',
        '7': '338px',
        '8': '360px',
        '9': '369px',
        '10': '415px',
        '11': '474px'
    },
    borderRadius: {
        full: '100px'
    },
    screens: {
        sm: '480px'
    },
    transitionDuration: {
        '200': '0.2s'
    },
    transitionTimingFunction: {
        default: 'ease'
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
