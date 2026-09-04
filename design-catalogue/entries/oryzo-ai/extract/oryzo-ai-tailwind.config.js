/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(25, 44%, 97%)',
            '100': 'hsl(25, 44%, 94%)',
            '200': 'hsl(25, 44%, 86%)',
            '300': 'hsl(25, 44%, 76%)',
            '400': 'hsl(25, 44%, 64%)',
            '500': 'hsl(25, 44%, 50%)',
            '600': 'hsl(25, 44%, 40%)',
            '700': 'hsl(25, 44%, 32%)',
            '800': 'hsl(25, 44%, 24%)',
            '900': 'hsl(25, 44%, 16%)',
            '950': 'hsl(25, 44%, 10%)',
            DEFAULT: '#382416'
        },
        secondary: {
            '50': 'hsl(33, 100%, 97%)',
            '100': 'hsl(33, 100%, 94%)',
            '200': 'hsl(33, 100%, 86%)',
            '300': 'hsl(33, 100%, 76%)',
            '400': 'hsl(33, 100%, 64%)',
            '500': 'hsl(33, 100%, 50%)',
            '600': 'hsl(33, 100%, 40%)',
            '700': 'hsl(33, 100%, 32%)',
            '800': 'hsl(33, 100%, 24%)',
            '900': 'hsl(33, 100%, 16%)',
            '950': 'hsl(33, 100%, 10%)',
            DEFAULT: '#ffedd7'
        },
        accent: {
            '50': 'hsl(22, 100%, 97%)',
            '100': 'hsl(22, 100%, 94%)',
            '200': 'hsl(22, 100%, 86%)',
            '300': 'hsl(22, 100%, 76%)',
            '400': 'hsl(22, 100%, 64%)',
            '500': 'hsl(22, 100%, 50%)',
            '600': 'hsl(22, 100%, 40%)',
            '700': 'hsl(22, 100%, 32%)',
            '800': 'hsl(22, 100%, 24%)',
            '900': 'hsl(22, 100%, 16%)',
            '950': 'hsl(22, 100%, 10%)',
            DEFAULT: '#dc5000'
        },
        'neutral-50': '#100904',
        'neutral-100': '#445231',
        'neutral-200': '#bbac97',
        'neutral-300': '#6c5f51',
        'neutral-400': '#000000',
        'neutral-500': '#5d6c49',
        'neutral-600': '#201914',
        background: '#100904',
        foreground: '#ffedd7'
    },
    fontFamily: {
        sans: [
            'halyard-display-variable',
            'sans-serif'
        ],
        body: [
            'DM Mono',
            'sans-serif'
        ]
    },
    fontSize: {
        '30': [
            '30px',
            {
                lineHeight: '30px'
            }
        ],
        '32': [
            '32px',
            {
                lineHeight: '34.88px'
            }
        ],
        '192': [
            '192px',
            {
                lineHeight: '192px',
                letterSpacing: '3.456px'
            }
        ],
        '364': [
            '364px',
            {
                lineHeight: '364px'
            }
        ],
        '201.481': [
            '201.481px',
            {
                lineHeight: '241.778px'
            }
        ],
        '130.37': [
            '130.37px',
            {
                lineHeight: '156.444px'
            }
        ],
        '109.333': [
            '109.333px',
            {
                lineHeight: '98.4px',
                letterSpacing: '-1.968px'
            }
        ],
        '57.1437': [
            '57.1437px',
            {
                lineHeight: '68.5724px'
            }
        ],
        '45.3333': [
            '45.3333px',
            {
                lineHeight: '45.3333px'
            }
        ],
        '43.7333': [
            '43.7333px',
            {
                lineHeight: '39.36px',
                letterSpacing: '-1.968px'
            }
        ],
        '42.88': [
            '42.88px',
            {
                lineHeight: '51.456px'
            }
        ],
        '38.6735': [
            '38.6735px',
            {
                lineHeight: '46.4081px'
            }
        ],
        '36.2667': [
            '36.2667px',
            {
                lineHeight: '32.64px'
            }
        ],
        '32.5178': [
            '32.5178px',
            {
                lineHeight: '76.8px'
            }
        ],
        '25.3333': [
            '25.3333px',
            {
                lineHeight: '31.996px'
            }
        ]
    },
    spacing: {
        '9': '36px',
        '10': '40px',
        '12': '48px',
        '14': '56px',
        '15': '60px',
        '16': '64px',
        '19': '76px',
        '24': '96px',
        '70': '280px',
        '91': '364px',
        '100': '400px',
        '101': '404px',
        '1px': '1px',
        '27px': '27px',
        '43px': '43px',
        '69px': '69px',
        '107px': '107px',
        '181px': '181px'
    },
    borderRadius: {
        lg: '12px',
        xl: '20px',
        full: '100px'
    },
    boxShadow: {
        xs: 'rgb(255, 160, 0) 0px 0px 3px 2px inset, rgb(224, 112, 16) 0px 0px 8px 4px inset',
        sm: 'rgba(255, 160, 0, 0.6) 0px 0px 5px 2px inset, rgb(224, 112, 16) 0px 0px 15px 8px inset, rgba(230, 100, 10, 0.45) 0px 0px 35px 15px inset, rgba(230, 80, 10, 0.35) 0px 0px 45px 20px inset',
        md: 'rgba(255, 140, 0, 0.6) 0px 0px 10px 3px, rgba(230, 80, 10, 0.25) 0px 0px 60px 45px'
    },
    transitionDuration: {
        '150': '0.15s',
        '180': '0.18s',
        '200': '0.2s',
        '250': '0.25s',
        '300': '0.3s',
        '500': '0.5s'
    },
    transitionTimingFunction: {
        default: 'ease'
    }
},
  },
};
