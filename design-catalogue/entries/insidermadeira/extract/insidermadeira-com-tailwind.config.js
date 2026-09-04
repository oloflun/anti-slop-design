/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(0, 100%, 97%)',
            '100': 'hsl(0, 100%, 94%)',
            '200': 'hsl(0, 100%, 86%)',
            '300': 'hsl(0, 100%, 76%)',
            '400': 'hsl(0, 100%, 64%)',
            '500': 'hsl(0, 100%, 50%)',
            '600': 'hsl(0, 100%, 40%)',
            '700': 'hsl(0, 100%, 32%)',
            '800': 'hsl(0, 100%, 24%)',
            '900': 'hsl(0, 100%, 16%)',
            '950': 'hsl(0, 100%, 10%)',
            DEFAULT: '#ffdede'
        },
        secondary: {
            '50': 'hsl(40, 30%, 97%)',
            '100': 'hsl(40, 30%, 94%)',
            '200': 'hsl(40, 30%, 86%)',
            '300': 'hsl(40, 30%, 76%)',
            '400': 'hsl(40, 30%, 64%)',
            '500': 'hsl(40, 30%, 50%)',
            '600': 'hsl(40, 30%, 40%)',
            '700': 'hsl(40, 30%, 32%)',
            '800': 'hsl(40, 30%, 24%)',
            '900': 'hsl(40, 30%, 16%)',
            '950': 'hsl(40, 30%, 10%)',
            DEFAULT: '#f1ede5'
        },
        'neutral-50': '#000000',
        'neutral-100': '#201f1d',
        'neutral-200': '#ffffff',
        'neutral-300': '#c6c3bb',
        'neutral-400': '#333333',
        'neutral-500': '#dddddd',
        'neutral-600': '#b8b8b8',
        'neutral-700': '#6a6a6a',
        'neutral-800': '#cccccc',
        background: '#f9f9f9',
        foreground: '#000000'
    },
    fontFamily: {
        body: [
            'PP Mori',
            'sans-serif'
        ],
        heading: [
            'GT Super Display',
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
        '14': [
            '14px',
            {
                lineHeight: '14px'
            }
        ],
        '16': [
            '16px',
            {
                lineHeight: 'normal'
            }
        ],
        '21': [
            '21px',
            {
                lineHeight: '27.3px'
            }
        ],
        '24': [
            '24px',
            {
                lineHeight: '31.2px'
            }
        ],
        '36': [
            '36px',
            {
                lineHeight: '36px'
            }
        ],
        '63.3333': [
            '63.3333px',
            {
                lineHeight: '63.3333px'
            }
        ],
        '23.4667': [
            '23.4667px',
            {
                lineHeight: '28.16px'
            }
        ],
        '12.8': [
            '12.8px',
            {
                lineHeight: '16.64px'
            }
        ],
        '10.6667': [
            '10.6667px',
            {
                lineHeight: '13.8667px'
            }
        ],
        '9.33333': [
            '9.33333px',
            {
                lineHeight: '11.2px'
            }
        ],
        '6.66667': [
            '6.66667px',
            {
                lineHeight: '6.66667px'
            }
        ]
    },
    spacing: {
        '0': '1px',
        '1': '24px',
        '2': '27px',
        '3': '30px',
        '4': '40px',
        '5': '53px',
        '6': '60px',
        '7': '67px',
        '8': '80px',
        '9': '85px',
        '10': '93px',
        '11': '100px',
        '12': '103px',
        '13': '149px',
        '14': '297px',
        '15': '333px',
        '16': '461px'
    },
    borderRadius: {
        sm: '3px',
        xl: '20px',
        full: '15984px'
    },
    screens: {
        lg: '992px'
    },
    transitionDuration: {
        '250': '0.25s',
        '500': '0.5s'
    },
    transitionTimingFunction: {
        default: 'ease'
    },
    container: {
        center: true,
        padding: '0px'
    },
    maxWidth: {
        container: '1226.67px'
    }
},
  },
};
