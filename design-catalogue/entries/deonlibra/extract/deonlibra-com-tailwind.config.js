/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(350, 99%, 97%)',
            '100': 'hsl(350, 99%, 94%)',
            '200': 'hsl(350, 99%, 86%)',
            '300': 'hsl(350, 99%, 76%)',
            '400': 'hsl(350, 99%, 64%)',
            '500': 'hsl(350, 99%, 50%)',
            '600': 'hsl(350, 99%, 40%)',
            '700': 'hsl(350, 99%, 32%)',
            '800': 'hsl(350, 99%, 24%)',
            '900': 'hsl(350, 99%, 16%)',
            '950': 'hsl(350, 99%, 10%)',
            DEFAULT: '#c00121'
        },
        secondary: {
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
            DEFAULT: '#fff8e7'
        },
        accent: {
            '50': 'hsl(216, 94%, 97%)',
            '100': 'hsl(216, 94%, 94%)',
            '200': 'hsl(216, 94%, 86%)',
            '300': 'hsl(216, 94%, 76%)',
            '400': 'hsl(216, 94%, 64%)',
            '500': 'hsl(216, 94%, 50%)',
            '600': 'hsl(216, 94%, 40%)',
            '700': 'hsl(216, 94%, 32%)',
            '800': 'hsl(216, 94%, 24%)',
            '900': 'hsl(216, 94%, 16%)',
            '950': 'hsl(216, 94%, 10%)',
            DEFAULT: '#146ff8'
        },
        'neutral-50': '#000000',
        'neutral-100': '#ffffff',
        'neutral-200': '#66635c',
        'neutral-300': '#808080',
        'neutral-400': '#f0f0f0',
        'neutral-500': '#1f2533',
        'neutral-600': '#949494',
        'neutral-700': '#c9c9c9',
        'neutral-800': '#fee9e8',
        background: '#fff8e7',
        foreground: '#000000'
    },
    fontFamily: {
        body: [
            'Roboto',
            'sans-serif'
        ],
        font2: [
            'Anton',
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
        '15': [
            '15px',
            {
                lineHeight: '15px'
            }
        ],
        '16': [
            '16px',
            {
                lineHeight: '26px'
            }
        ],
        '18': [
            '18px',
            {
                lineHeight: '27px'
            }
        ],
        '22': [
            '22px',
            {
                lineHeight: '35.75px'
            }
        ],
        '28': [
            '28px',
            {
                lineHeight: '38.0016px',
                letterSpacing: '-1.12px'
            }
        ],
        '32': [
            '32px',
            {
                lineHeight: '32px'
            }
        ],
        '40': [
            '40px',
            {
                lineHeight: '48px',
                letterSpacing: '-1.6px'
            }
        ],
        '48': [
            '48px',
            {
                lineHeight: '60px',
                letterSpacing: '-1.92px'
            }
        ],
        '60': [
            '60px',
            {
                lineHeight: '72px',
                letterSpacing: '-2.4px'
            }
        ],
        '19.2': [
            '19.2px',
            {
                lineHeight: '30px'
            }
        ],
        '17.92': [
            '17.92px',
            {
                lineHeight: '27.92px',
                letterSpacing: '-0.7168px'
            }
        ],
        '14.4': [
            '14.4px',
            {
                lineHeight: '18px'
            }
        ],
        '13.6': [
            '13.6px',
            {
                lineHeight: '16.32px'
            }
        ],
        '13.3333': [
            '13.3333px',
            {
                lineHeight: 'normal'
            }
        ]
    },
    spacing: {
        '10': '20px',
        '12': '24px',
        '15': '30px',
        '20': '40px',
        '24': '48px',
        '28': '56px',
        '30': '60px',
        '35': '70px',
        '39': '78px',
        '42': '84px',
        '50': '100px',
        '1px': '1px',
        '287px': '287px'
    },
    borderRadius: {
        sm: '3px',
        md: '8px',
        xl: '24px',
        full: '50px'
    },
    boxShadow: {
        sm: 'rgba(19, 110, 248, 0.3) 0px 0px 0px 5px',
        lg: 'rgba(8, 19, 79, 0.16) 0px 4px 13.333px 0px'
    },
    screens: {
        md: '750px',
        lg: '1024px',
        '1200px': '1200px',
        xl: '1280px',
        '1410px': '1410px',
        '2xl': '1536px'
    },
    transitionDuration: {
        '100': '0.1s',
        '150': '0.15s',
        '200': '0.2s',
        '220': '0.22s',
        '250': '0.25s',
        '300': '0.3s',
        '500': '0.5s',
        '540': '0.54s',
        '600': '0.6s',
        '800': '0.8s'
    },
    transitionTimingFunction: {
        custom: 'cubic-bezier(0.4, 0, 0.2, 1)'
    },
    container: {
        center: true,
        padding: '0px'
    },
    maxWidth: {
        container: '460px'
    }
},
  },
};
