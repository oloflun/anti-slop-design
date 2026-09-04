/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(47, 100%, 97%)',
            '100': 'hsl(47, 100%, 94%)',
            '200': 'hsl(47, 100%, 86%)',
            '300': 'hsl(47, 100%, 76%)',
            '400': 'hsl(47, 100%, 64%)',
            '500': 'hsl(47, 100%, 50%)',
            '600': 'hsl(47, 100%, 40%)',
            '700': 'hsl(47, 100%, 32%)',
            '800': 'hsl(47, 100%, 24%)',
            '900': 'hsl(47, 100%, 16%)',
            '950': 'hsl(47, 100%, 10%)',
            DEFAULT: '#ffdb5b'
        },
        secondary: {
            '50': 'hsl(240, 100%, 97%)',
            '100': 'hsl(240, 100%, 94%)',
            '200': 'hsl(240, 100%, 86%)',
            '300': 'hsl(240, 100%, 76%)',
            '400': 'hsl(240, 100%, 64%)',
            '500': 'hsl(240, 100%, 50%)',
            '600': 'hsl(240, 100%, 40%)',
            '700': 'hsl(240, 100%, 32%)',
            '800': 'hsl(240, 100%, 24%)',
            '900': 'hsl(240, 100%, 16%)',
            '950': 'hsl(240, 100%, 10%)',
            DEFAULT: '#0000ee'
        },
        accent: {
            '50': 'hsl(54, 100%, 97%)',
            '100': 'hsl(54, 100%, 94%)',
            '200': 'hsl(54, 100%, 86%)',
            '300': 'hsl(54, 100%, 76%)',
            '400': 'hsl(54, 100%, 64%)',
            '500': 'hsl(54, 100%, 50%)',
            '600': 'hsl(54, 100%, 40%)',
            '700': 'hsl(54, 100%, 32%)',
            '800': 'hsl(54, 100%, 24%)',
            '900': 'hsl(54, 100%, 16%)',
            '950': 'hsl(54, 100%, 10%)',
            DEFAULT: '#fff386'
        },
        'neutral-50': '#202020',
        'neutral-100': '#575656',
        'neutral-200': '#343333',
        'neutral-300': '#ffffff',
        'neutral-400': '#f3f3f3',
        background: '#ffdb5b',
        foreground: '#343333'
    },
    fontFamily: {
        sans: [
            'BumbleSans',
            'sans-serif'
        ]
    },
    fontSize: {
        '15': [
            '15px',
            {
                lineHeight: '20px',
                letterSpacing: '0.3px'
            }
        ],
        '16': [
            '16px',
            {
                lineHeight: '24px'
            }
        ],
        '17': [
            '17px',
            {
                lineHeight: '20px',
                letterSpacing: '0.3px'
            }
        ],
        '18': [
            '18px',
            {
                lineHeight: '21.6px'
            }
        ],
        '20': [
            '20px',
            {
                lineHeight: '25px',
                letterSpacing: '0.32px'
            }
        ],
        '24': [
            '24px',
            {
                lineHeight: '24px'
            }
        ],
        '32': [
            '32px',
            {
                lineHeight: '48px'
            }
        ],
        '34': [
            '34px',
            {
                lineHeight: '34px',
                letterSpacing: '0.4px'
            }
        ],
        '40': [
            '40px',
            {
                lineHeight: '40px'
            }
        ],
        '49': [
            '49px',
            {
                lineHeight: '55px',
                letterSpacing: '0.42px'
            }
        ],
        '68': [
            '68px',
            {
                lineHeight: '70px',
                letterSpacing: '0.46px'
            }
        ]
    },
    spacing: {
        '3': '6px',
        '10': '20px',
        '16': '32px',
        '20': '40px',
        '24': '48px',
        '30': '60px',
        '1px': '1px'
    },
    borderRadius: {
        md: '9px',
        lg: '16px',
        xl: '24px',
        full: '1000px'
    },
    boxShadow: {
        sm: 'rgba(255, 255, 255, 0) 0px 0px 0px 0px',
        md: 'rgba(32, 32, 32, 0.12) 0px 1px 8px 0px'
    },
    screens: {
        '412px': '412px',
        sm: '680px',
        md: '780px',
        '900px': '900px',
        lg: '1024px',
        '1200px': '1200px',
        xl: '1320px',
        '1360px': '1360px',
        '1420px': '1420px'
    },
    transitionDuration: {
        '200': '0.2s',
        '300': '0.3s'
    },
    transitionTimingFunction: {
        default: 'ease'
    },
    container: {
        center: true,
        padding: '0px'
    },
    maxWidth: {
        container: '1360px'
    }
},
  },
};
