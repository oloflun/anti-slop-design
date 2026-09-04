/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(0, 14%, 97%)',
            '100': 'hsl(0, 14%, 94%)',
            '200': 'hsl(0, 14%, 86%)',
            '300': 'hsl(0, 14%, 76%)',
            '400': 'hsl(0, 14%, 64%)',
            '500': 'hsl(0, 14%, 50%)',
            '600': 'hsl(0, 14%, 40%)',
            '700': 'hsl(0, 14%, 32%)',
            '800': 'hsl(0, 14%, 24%)',
            '900': 'hsl(0, 14%, 16%)',
            '950': 'hsl(0, 14%, 10%)',
            DEFAULT: '#191313'
        },
        'neutral-50': '#efeeec',
        'neutral-100': '#a8a99e',
        'neutral-200': '#000000',
        background: '#a8a99e',
        foreground: '#000000'
    },
    fontFamily: {
        sans: [
            'Times Now',
            'sans-serif'
        ],
        heading: [
            'Inter Tight',
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
        '49': [
            '49px',
            {
                lineHeight: '49px',
                letterSpacing: '-2.45px'
            }
        ],
        '22.75': [
            '22.75px',
            {
                lineHeight: '22.75px',
                letterSpacing: '-0.2275px'
            }
        ],
        '17.5': [
            '17.5px',
            {
                lineHeight: '17.5px',
                letterSpacing: '-0.175px'
            }
        ],
        '15.75': [
            '15.75px',
            {
                lineHeight: '18.9px',
                letterSpacing: '-0.4725px'
            }
        ],
        '12.25': [
            '12.25px',
            {
                lineHeight: '14.7px',
                letterSpacing: '-0.42px'
            }
        ],
        '10.5': [
            '10.5px',
            {
                lineHeight: '13.125px',
                letterSpacing: '0.21px'
            }
        ]
    },
    spacing: {
        '0': '1px',
        '1': '28px',
        '2': '35px',
        '3': '70px',
        '4': '88px',
        '5': '105px',
        '6': '112px',
        '7': '119px',
        '8': '140px',
        '9': '154px',
        '10': '168px',
        '11': '175px',
        '12': '191px',
        '13': '201px',
        '14': '236px',
        '15': '252px',
        '16': '296px',
        '17': '335px',
        '18': '343px',
        '19': '387px',
        '20': '394px',
        '21': '456px'
    },
    screens: {
        md: '768px',
        lg: '992px',
        '2xl': '1600px'
    },
    transitionDuration: {
        '40': '0.04s',
        '80': '0.08s',
        '120': '0.12s',
        '150': '0.15s',
        '160': '0.16s',
        '200': '0.2s',
        '240': '0.24s',
        '250': '0.25s',
        '280': '0.28s',
        '300': '0.3s',
        '320': '0.32s',
        '350': '0.35s',
        '450': '0.45s',
        '550': '0.55s',
        '800': '0.8s',
        '1000': '1s'
    },
    transitionTimingFunction: {
        custom: 'cubic-bezier(0.075, 0.82, 0.165, 1)',
        linear: 'linear'
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
