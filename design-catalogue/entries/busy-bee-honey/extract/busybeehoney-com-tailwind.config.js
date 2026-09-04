/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(42, 100%, 97%)',
            '100': 'hsl(42, 100%, 94%)',
            '200': 'hsl(42, 100%, 86%)',
            '300': 'hsl(42, 100%, 76%)',
            '400': 'hsl(42, 100%, 64%)',
            '500': 'hsl(42, 100%, 50%)',
            '600': 'hsl(42, 100%, 40%)',
            '700': 'hsl(42, 100%, 32%)',
            '800': 'hsl(42, 100%, 24%)',
            '900': 'hsl(42, 100%, 16%)',
            '950': 'hsl(42, 100%, 10%)',
            DEFAULT: '#ffca50'
        },
        secondary: {
            '50': 'hsl(12, 27%, 97%)',
            '100': 'hsl(12, 27%, 94%)',
            '200': 'hsl(12, 27%, 86%)',
            '300': 'hsl(12, 27%, 76%)',
            '400': 'hsl(12, 27%, 64%)',
            '500': 'hsl(12, 27%, 50%)',
            '600': 'hsl(12, 27%, 40%)',
            '700': 'hsl(12, 27%, 32%)',
            '800': 'hsl(12, 27%, 24%)',
            '900': 'hsl(12, 27%, 16%)',
            '950': 'hsl(12, 27%, 10%)',
            DEFAULT: '#3b2722'
        },
        accent: {
            '50': 'hsl(5, 58%, 97%)',
            '100': 'hsl(5, 58%, 94%)',
            '200': 'hsl(5, 58%, 86%)',
            '300': 'hsl(5, 58%, 76%)',
            '400': 'hsl(5, 58%, 64%)',
            '500': 'hsl(5, 58%, 50%)',
            '600': 'hsl(5, 58%, 40%)',
            '700': 'hsl(5, 58%, 32%)',
            '800': 'hsl(5, 58%, 24%)',
            '900': 'hsl(5, 58%, 16%)',
            '950': 'hsl(5, 58%, 10%)',
            DEFAULT: '#a0342a'
        },
        'neutral-50': '#000000',
        'neutral-100': '#6fa162',
        background: '#f2ebd0',
        foreground: '#000000'
    },
    fontFamily: {
        body: [
            'AnonymousPro-Regular',
            'sans-serif'
        ],
        heading: [
            'TayBirdie-Regular',
            'sans-serif'
        ],
        font2: [
            'TayMakawao-Regular',
            'sans-serif'
        ]
    },
    fontSize: {
        '14': [
            '14px',
            {
                lineHeight: '14px'
            }
        ],
        '15': [
            '15px',
            {
                lineHeight: '15px'
            }
        ],
        '16': [
            '16px',
            {
                lineHeight: 'normal'
            }
        ],
        '24': [
            '24px',
            {
                lineHeight: '24px'
            }
        ],
        '65': [
            '65px',
            {
                lineHeight: '65px'
            }
        ],
        '185': [
            '185px',
            {
                lineHeight: '148px',
                letterSpacing: '-1.85px'
            }
        ],
        '210': [
            '210px',
            {
                lineHeight: '210px'
            }
        ],
        '112.667': [
            '112.667px',
            {
                lineHeight: '92.3867px'
            }
        ],
        '76.6667': [
            '76.6667px',
            {
                lineHeight: '62.8667px'
            }
        ],
        '25.3333': [
            '25.3333px',
            {
                lineHeight: '25.3333px'
            }
        ],
        '18.6667': [
            '18.6667px',
            {
                lineHeight: '20.5333px'
            }
        ],
        '15.3333': [
            '15.3333px',
            {
                lineHeight: '24.6867px',
                letterSpacing: '0.5px'
            }
        ],
        '13.6667': [
            '13.6667px',
            {
                lineHeight: '20.5px'
            }
        ],
        '13.3333': [
            '13.3333px',
            {
                lineHeight: '16px'
            }
        ],
        '12.6667': [
            '12.6667px',
            {
                lineHeight: '12.6667px'
            }
        ]
    },
    spacing: {
        '3': '6px',
        '30': '60px',
        '40': '80px',
        '109': '218px'
    },
    borderRadius: {
        full: '1000px'
    },
    screens: {
        sm: '700px',
        lg: '960px',
        '1410px': '1410px',
        '1440px': '1440px',
        '1920px': '1920px'
    },
    transitionDuration: {
        '200': '0.2s',
        '300': '0.3s',
        '400': '0.4s',
        '500': '0.5s',
        '700': '0.7s',
        '1000': '1s'
    },
    transitionTimingFunction: {
        default: 'ease',
        custom: 'cubic-bezier(0.25, 0.46, 0.45, 0.94)'
    },
    container: {
        center: true,
        padding: '0px'
    },
    maxWidth: {
        container: '1000px'
    }
},
  },
};
