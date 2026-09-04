/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        'neutral-50': '#000000',
        'neutral-100': '#ffffff',
        'neutral-200': '#3c3c3c',
        'neutral-300': '#efefef',
        'neutral-400': '#adadad',
        'neutral-500': '#101010',
        background: '#ffffff',
        foreground: '#000000'
    },
    fontFamily: {
        sans: [
            'Body Font',
            'sans-serif'
        ],
        body: [
            'Button Font',
            'sans-serif'
        ],
        heading: [
            'Heading Font',
            'sans-serif'
        ]
    },
    fontSize: {
        '9': [
            '9px',
            {
                lineHeight: '11.52px'
            }
        ],
        '10': [
            '10px',
            {
                lineHeight: '14px'
            }
        ],
        '12': [
            '12px',
            {
                lineHeight: '15px'
            }
        ],
        '14': [
            '14px',
            {
                lineHeight: '18.2px'
            }
        ],
        '16': [
            '16px',
            {
                lineHeight: '20.8px'
            }
        ],
        '20': [
            '20px',
            {
                lineHeight: '35px'
            }
        ],
        '22': [
            '22px',
            {
                lineHeight: '27px',
                letterSpacing: '-1px'
            }
        ],
        '28': [
            '28px',
            {
                lineHeight: '33px',
                letterSpacing: '-1px'
            }
        ],
        '10.0002': [
            '10.0002px',
            {
                lineHeight: '18.2px'
            }
        ]
    },
    spacing: {
        '12': '24px',
        '14': '28px',
        '16': '32px',
        '18': '36px',
        '20': '40px',
        '24': '48px',
        '32': '64px',
        '64': '128px',
        '145': '290px',
        '158': '316px',
        '167': '334px',
        '1px': '1px',
        '57px': '57px'
    },
    borderRadius: {
        lg: '12px',
        full: '50px'
    },
    boxShadow: {
        md: 'rgba(0, 0, 0, 0.1) 0px 4px 10px 0px',
        xl: 'rgba(0, 0, 0, 0.2) 0px 26px 80px 0px'
    },
    screens: {
        sm: '600px',
        '905px': '905px',
        lg: '1044px',
        xl: '1281px',
        '1440px': '1440px',
        '1920px': '1920px'
    },
    transitionDuration: {
        '100': '0.1s',
        '150': '0.15s',
        '200': '0.2s',
        '250': '0.25s',
        '300': '0.3s',
        '350': '0.35s',
        '400': '0.4s',
        '500': '0.5s',
        '600': '0.6s',
        '800': '0.8s',
        '1000': '1s'
    },
    transitionTimingFunction: {
        default: 'ease',
        custom: 'cubic-bezier(0.37, 0, 0, 1)',
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
