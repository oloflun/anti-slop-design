/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(5, 78%, 97%)',
            '100': 'hsl(5, 78%, 94%)',
            '200': 'hsl(5, 78%, 86%)',
            '300': 'hsl(5, 78%, 76%)',
            '400': 'hsl(5, 78%, 64%)',
            '500': 'hsl(5, 78%, 50%)',
            '600': 'hsl(5, 78%, 40%)',
            '700': 'hsl(5, 78%, 32%)',
            '800': 'hsl(5, 78%, 24%)',
            '900': 'hsl(5, 78%, 16%)',
            '950': 'hsl(5, 78%, 10%)',
            DEFAULT: '#ef8a80'
        },
        secondary: {
            '50': 'hsl(51, 63%, 97%)',
            '100': 'hsl(51, 63%, 94%)',
            '200': 'hsl(51, 63%, 86%)',
            '300': 'hsl(51, 63%, 76%)',
            '400': 'hsl(51, 63%, 64%)',
            '500': 'hsl(51, 63%, 50%)',
            '600': 'hsl(51, 63%, 40%)',
            '700': 'hsl(51, 63%, 32%)',
            '800': 'hsl(51, 63%, 24%)',
            '900': 'hsl(51, 63%, 16%)',
            '950': 'hsl(51, 63%, 10%)',
            DEFAULT: '#dcca65'
        },
        accent: {
            '50': 'hsl(216, 60%, 97%)',
            '100': 'hsl(216, 60%, 94%)',
            '200': 'hsl(216, 60%, 86%)',
            '300': 'hsl(216, 60%, 76%)',
            '400': 'hsl(216, 60%, 64%)',
            '500': 'hsl(216, 60%, 50%)',
            '600': 'hsl(216, 60%, 40%)',
            '700': 'hsl(216, 60%, 32%)',
            '800': 'hsl(216, 60%, 24%)',
            '900': 'hsl(216, 60%, 16%)',
            '950': 'hsl(216, 60%, 10%)',
            DEFAULT: '#326ec8'
        },
        'neutral-50': '#f2f0ed',
        'neutral-100': '#ffffff',
        'neutral-200': '#111111',
        'neutral-300': '#272727',
        'neutral-400': '#000000',
        'neutral-500': '#343434',
        'neutral-600': '#1b1b1b',
        'neutral-700': '#909090',
        'neutral-800': '#777777',
        'neutral-900': '#b2b2b2',
        background: '#121212',
        foreground: '#ffffff'
    },
    fontFamily: {
        sans: [
            'geistMono',
            'sans-serif'
        ],
        body: [
            'monologueSerifItalic',
            'sans-serif'
        ],
        mono: [
            'monologueSerif',
            'sans-serif'
        ]
    },
    fontSize: {
        '16': [
            '16px',
            {
                lineHeight: 'normal'
            }
        ],
        '18': [
            '18px',
            {
                lineHeight: 'normal',
                letterSpacing: '-0.54px'
            }
        ],
        '20': [
            '20px',
            {
                lineHeight: '20px',
                letterSpacing: '-0.2px'
            }
        ],
        '24': [
            '24px',
            {
                lineHeight: '37.2px',
                letterSpacing: '-0.72px'
            }
        ],
        '26': [
            '26px',
            {
                lineHeight: 'normal'
            }
        ],
        '28': [
            '28px',
            {
                lineHeight: '28px',
                letterSpacing: '-0.98px'
            }
        ],
        '32': [
            '32px',
            {
                lineHeight: '30.4px',
                letterSpacing: '-0.96px'
            }
        ],
        '46': [
            '46px',
            {
                lineHeight: '46px'
            }
        ],
        '48': [
            '48px',
            {
                lineHeight: '43.2px',
                letterSpacing: '-1.44px'
            }
        ],
        '52': [
            '52px',
            {
                lineHeight: '49.4px',
                letterSpacing: '-1.56px'
            }
        ],
        '72': [
            '72px',
            {
                lineHeight: '72px',
                letterSpacing: '-1.44px'
            }
        ],
        '92': [
            '92px',
            {
                lineHeight: '71.76px',
                letterSpacing: '-2.76px'
            }
        ],
        '46.44': [
            '46.44px',
            {
                lineHeight: '46.44px',
                letterSpacing: '-1.44px'
            }
        ],
        '38.095': [
            '38.095px',
            {
                lineHeight: '34.2855px',
                letterSpacing: '-1.5238px'
            }
        ],
        '22.291': [
            '22.291px',
            {
                lineHeight: 'normal',
                letterSpacing: '-0.6687px'
            }
        ]
    },
    spacing: {
        '13': '26px',
        '20': '40px',
        '25': '50px',
        '26': '52px',
        '29': '58px',
        '30': '60px',
        '32': '64px',
        '33': '66px',
        '36': '72px',
        '40': '80px',
        '52': '104px',
        '151': '302px',
        '160': '320px',
        '1px': '1px',
        '19px': '19px',
        '31px': '31px',
        '35px': '35px',
        '47px': '47px',
        '75px': '75px',
        '107px': '107px',
        '127px': '127px'
    },
    borderRadius: {
        xs: '1px',
        sm: '4px',
        md: '10px',
        lg: '14px',
        xl: '22px',
        full: '999px'
    },
    boxShadow: {
        xs: 'rgba(255, 255, 255, 0.25) -1px 0px 1px 0px, rgba(255, 255, 255, 0.25) 1px 0px 1px 0px, rgba(255, 255, 255, 0.25) 0px -1px 0.5px 0px inset',
        sm: 'rgba(0, 0, 0, 0.1) 0px 1px 4px 0px',
        md: 'rgba(0, 0, 0, 0.19) 0px 4px 8px 0px, rgba(0, 0, 0, 0.17) 0px 15px 15px 0px, rgba(0, 0, 0, 0.1) 0px 34px 20px 0px, rgba(0, 0, 0, 0.03) 0px 60px 24px 0px',
        lg: 'rgba(0, 0, 0, 0.42) 0px 12px 18px 0px',
        xl: 'rgba(0, 0, 0, 0.04) 0px 208px 83px 0px, rgba(0, 0, 0, 0.14) 0px 117px 70px 0px, rgba(0, 0, 0, 0.23) 0px 52px 52px 0px, rgba(0, 0, 0, 0.27) 0px 13px 29px 0px'
    },
    screens: {
        xs: '361px',
        sm: '481px',
        md: '761px'
    },
    transitionDuration: {
        '40': '0.04s',
        '70': '0.07s',
        '90': '0.09s',
        '120': '0.12s',
        '140': '0.14s',
        '160': '0.16s',
        '180': '0.18s',
        '220': '0.22s',
        '240': '0.24s',
        '260': '0.26s',
        '280': '0.28s',
        '320': '0.32s',
        '460': '0.46s',
        '620': '0.62s'
    },
    transitionTimingFunction: {
        custom: 'cubic-bezier(0.77, 0, 0.175, 1)',
        default: 'ease'
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
