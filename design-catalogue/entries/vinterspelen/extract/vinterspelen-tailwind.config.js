/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(19, 100%, 97%)',
            '100': 'hsl(19, 100%, 94%)',
            '200': 'hsl(19, 100%, 86%)',
            '300': 'hsl(19, 100%, 76%)',
            '400': 'hsl(19, 100%, 64%)',
            '500': 'hsl(19, 100%, 50%)',
            '600': 'hsl(19, 100%, 40%)',
            '700': 'hsl(19, 100%, 32%)',
            '800': 'hsl(19, 100%, 24%)',
            '900': 'hsl(19, 100%, 16%)',
            '950': 'hsl(19, 100%, 10%)',
            DEFAULT: '#290d00'
        },
        secondary: {
            '50': 'hsl(33, 81%, 97%)',
            '100': 'hsl(33, 81%, 94%)',
            '200': 'hsl(33, 81%, 86%)',
            '300': 'hsl(33, 81%, 76%)',
            '400': 'hsl(33, 81%, 64%)',
            '500': 'hsl(33, 81%, 50%)',
            '600': 'hsl(33, 81%, 40%)',
            '700': 'hsl(33, 81%, 32%)',
            '800': 'hsl(33, 81%, 24%)',
            '900': 'hsl(33, 81%, 16%)',
            '950': 'hsl(33, 81%, 10%)',
            DEFAULT: '#b36b13'
        },
        accent: {
            '50': 'hsl(40, 31%, 97%)',
            '100': 'hsl(40, 31%, 94%)',
            '200': 'hsl(40, 31%, 86%)',
            '300': 'hsl(40, 31%, 76%)',
            '400': 'hsl(40, 31%, 64%)',
            '500': 'hsl(40, 31%, 50%)',
            '600': 'hsl(40, 31%, 40%)',
            '700': 'hsl(40, 31%, 32%)',
            '800': 'hsl(40, 31%, 24%)',
            '900': 'hsl(40, 31%, 16%)',
            '950': 'hsl(40, 31%, 10%)',
            DEFAULT: '#d2c4a9'
        },
        'neutral-50': '#e5e7eb',
        'neutral-100': '#050302',
        'neutral-200': '#6c6557',
        'neutral-300': '#b2a285',
        background: '#010304',
        foreground: '#000000'
    },
    fontFamily: {
        body: [
            'Newsreader',
            'sans-serif'
        ],
        heading: [
            'Bodoni Moda',
            'sans-serif'
        ]
    },
    fontSize: {
        '13': [
            '13px',
            {
                lineHeight: '19.5px',
                letterSpacing: '5.46px'
            }
        ],
        '16': [
            '16px',
            {
                lineHeight: '24px'
            }
        ],
        '18': [
            '18px',
            {
                lineHeight: '27px'
            }
        ],
        '19': [
            '19px',
            {
                lineHeight: '30.875px',
                letterSpacing: '-0.266px'
            }
        ],
        '21': [
            '21px',
            {
                lineHeight: '31.5px',
                letterSpacing: '-0.294px'
            }
        ],
        '23': [
            '23px',
            {
                lineHeight: '23px'
            }
        ],
        '64': [
            '64px',
            {
                lineHeight: '63.36px',
                letterSpacing: '-0.896px'
            }
        ],
        '101.12': [
            '101.12px',
            {
                lineHeight: '95.0528px',
                letterSpacing: '-1.41568px'
            }
        ],
        '81.92': [
            '81.92px',
            {
                lineHeight: '70.4512px',
                letterSpacing: '-1.6384px'
            }
        ],
        '44.8': [
            '44.8px',
            {
                lineHeight: '38.528px',
                letterSpacing: '-0.896px'
            }
        ],
        '39.04': [
            '39.04px',
            {
                lineHeight: '41.3824px',
                letterSpacing: '-0.54656px'
            }
        ],
        '24.32': [
            '24.32px',
            {
                lineHeight: '28.2112px',
                letterSpacing: '-0.34048px'
            }
        ],
        '15.5': [
            '15.5px',
            {
                lineHeight: '25.73px'
            }
        ],
        '12.5': [
            '12.5px',
            {
                lineHeight: '19.375px'
            }
        ],
        '11.5': [
            '11.5px',
            {
                lineHeight: '17.25px',
                letterSpacing: '2.7025px'
            }
        ]
    },
    spacing: {
        '1': '2px',
        '28': '56px',
        '32': '64px',
        '40': '80px',
        '48': '96px',
        '56': '112px',
        '64': '128px',
        '120': '240px',
        '129': '258px',
        '121px': '121px'
    },
    boxShadow: {
        sm: 'oklab(0.42 0.0327558 0.100812 / 0.45) 0px 0px 0px 1px'
    },
    screens: {
        sm: '640px',
        md: '768px',
        lg: '1024px',
        xl: '1280px'
    },
    transitionDuration: {
        '120': '0.12s',
        '150': '0.15s',
        '320': '0.32s',
        '350': '0.35s',
        '1300': '1.3s'
    },
    transitionTimingFunction: {
        custom: 'cubic-bezier(0.16, 1, 0.3, 1)'
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
