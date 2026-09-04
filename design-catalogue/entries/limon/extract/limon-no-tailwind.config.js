/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(56, 92%, 97%)',
            '100': 'hsl(56, 92%, 94%)',
            '200': 'hsl(56, 92%, 86%)',
            '300': 'hsl(56, 92%, 76%)',
            '400': 'hsl(56, 92%, 64%)',
            '500': 'hsl(56, 92%, 50%)',
            '600': 'hsl(56, 92%, 40%)',
            '700': 'hsl(56, 92%, 32%)',
            '800': 'hsl(56, 92%, 24%)',
            '900': 'hsl(56, 92%, 16%)',
            '950': 'hsl(56, 92%, 10%)',
            DEFAULT: '#f7ea48'
        },
        secondary: {
            '50': 'hsl(127, 57%, 97%)',
            '100': 'hsl(127, 57%, 94%)',
            '200': 'hsl(127, 57%, 86%)',
            '300': 'hsl(127, 57%, 76%)',
            '400': 'hsl(127, 57%, 64%)',
            '500': 'hsl(127, 57%, 50%)',
            '600': 'hsl(127, 57%, 40%)',
            '700': 'hsl(127, 57%, 32%)',
            '800': 'hsl(127, 57%, 24%)',
            '900': 'hsl(127, 57%, 16%)',
            '950': 'hsl(127, 57%, 10%)',
            DEFAULT: '#103b15'
        },
        accent: {
            '50': 'hsl(353, 45%, 97%)',
            '100': 'hsl(353, 45%, 94%)',
            '200': 'hsl(353, 45%, 86%)',
            '300': 'hsl(353, 45%, 76%)',
            '400': 'hsl(353, 45%, 64%)',
            '500': 'hsl(353, 45%, 50%)',
            '600': 'hsl(353, 45%, 40%)',
            '700': 'hsl(353, 45%, 32%)',
            '800': 'hsl(353, 45%, 24%)',
            '900': 'hsl(353, 45%, 16%)',
            '950': 'hsl(353, 45%, 10%)',
            DEFAULT: '#1d0b0d'
        },
        'neutral-50': '#000000',
        'neutral-100': '#fcf9f0',
        'neutral-200': '#dbe2dc',
        'neutral-300': '#ffffff',
        background: '#1d0b0d',
        foreground: '#000000'
    },
    fontFamily: {
        sans: [
            'VenusCom',
            'sans-serif'
        ],
        body: [
            'FreeSans',
            'sans-serif'
        ]
    },
    fontSize: {
        '14': [
            '14px',
            {
                lineHeight: '19.2px',
                letterSpacing: '0.56px'
            }
        ],
        '16': [
            '16px',
            {
                lineHeight: 'normal'
            }
        ],
        '19': [
            '19px',
            {
                lineHeight: '19.2px',
                letterSpacing: '0.38px'
            }
        ],
        '20': [
            '20px',
            {
                lineHeight: '29px'
            }
        ],
        '26': [
            '26px',
            {
                lineHeight: '33.8px'
            }
        ],
        '30': [
            '30px',
            {
                lineHeight: '40.5px'
            }
        ],
        '36': [
            '36px',
            {
                lineHeight: '43.2px'
            }
        ],
        '46': [
            '46px',
            {
                lineHeight: '52.9px'
            }
        ],
        '54': [
            '54px',
            {
                lineHeight: '54px'
            }
        ],
        '68': [
            '68px',
            {
                lineHeight: '81.6px',
                letterSpacing: '2.04px'
            }
        ],
        '75': [
            '75px',
            {
                lineHeight: '93.75px'
            }
        ]
    },
    spacing: {
        '0': '0px',
        '5': '25px',
        '6': '30px',
        '8': '40px',
        '9': '45px',
        '10': '50px',
        '12': '60px',
        '15': '75px',
        '16': '80px',
        '24': '120px',
        '33': '165px',
        '64': '320px',
        '144px': '144px'
    },
    borderRadius: {
        xs: '1px',
        full: '100px'
    },
    screens: {
        '0px': '0px',
        xs: '376px',
        sm: '427px',
        '1200px': '1200px'
    },
    transitionDuration: {
        '250': '0.25s',
        '800': '0.8s',
        '1000': '1s'
    },
    transitionTimingFunction: {
        default: 'ease'
    },
    container: {
        center: true,
        padding: '0px'
    },
    maxWidth: {
        container: '1170px'
    }
},
  },
};
