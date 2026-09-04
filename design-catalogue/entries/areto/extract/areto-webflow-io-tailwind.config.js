/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(61, 92%, 97%)',
            '100': 'hsl(61, 92%, 94%)',
            '200': 'hsl(61, 92%, 86%)',
            '300': 'hsl(61, 92%, 76%)',
            '400': 'hsl(61, 92%, 64%)',
            '500': 'hsl(61, 92%, 50%)',
            '600': 'hsl(61, 92%, 40%)',
            '700': 'hsl(61, 92%, 32%)',
            '800': 'hsl(61, 92%, 24%)',
            '900': 'hsl(61, 92%, 16%)',
            '950': 'hsl(61, 92%, 10%)',
            DEFAULT: '#f8fa8d'
        },
        secondary: {
            '50': 'hsl(141, 19%, 97%)',
            '100': 'hsl(141, 19%, 94%)',
            '200': 'hsl(141, 19%, 86%)',
            '300': 'hsl(141, 19%, 76%)',
            '400': 'hsl(141, 19%, 64%)',
            '500': 'hsl(141, 19%, 50%)',
            '600': 'hsl(141, 19%, 40%)',
            '700': 'hsl(141, 19%, 32%)',
            '800': 'hsl(141, 19%, 24%)',
            '900': 'hsl(141, 19%, 16%)',
            '950': 'hsl(141, 19%, 10%)',
            DEFAULT: '#36503f'
        },
        accent: {
            '50': 'hsl(330, 29%, 97%)',
            '100': 'hsl(330, 29%, 94%)',
            '200': 'hsl(330, 29%, 86%)',
            '300': 'hsl(330, 29%, 76%)',
            '400': 'hsl(330, 29%, 64%)',
            '500': 'hsl(330, 29%, 50%)',
            '600': 'hsl(330, 29%, 40%)',
            '700': 'hsl(330, 29%, 32%)',
            '800': 'hsl(330, 29%, 24%)',
            '900': 'hsl(330, 29%, 16%)',
            '950': 'hsl(330, 29%, 10%)',
            DEFAULT: '#120a0e'
        },
        'neutral-50': '#000000',
        'neutral-100': '#4d4d4d',
        'neutral-200': '#ece7e4',
        'neutral-300': '#ffffff',
        'neutral-400': '#cccccc',
        'neutral-500': '#333333',
        'neutral-600': '#f5f5f5',
        'neutral-700': '#26382c',
        'neutral-800': '#dddddd',
        background: '#f5f5f5',
        foreground: '#000000'
    },
    fontFamily: {
        sans: [
            'Inter Tight',
            'sans-serif'
        ]
    },
    fontSize: {
        '13': [
            '13px',
            {
                lineHeight: '25.92px'
            }
        ],
        '14': [
            '14px',
            {
                lineHeight: '25.92px'
            }
        ],
        '16': [
            '16px',
            {
                lineHeight: 'normal'
            }
        ],
        '18': [
            '18px',
            {
                lineHeight: '22.86px',
                letterSpacing: '-0.54px'
            }
        ],
        '20': [
            '20px',
            {
                lineHeight: '25px',
                letterSpacing: '-0.60016px'
            }
        ],
        '24': [
            '24px',
            {
                lineHeight: '25.92px'
            }
        ],
        '29': [
            '29px',
            {
                lineHeight: '30.16px',
                letterSpacing: '-0.435px'
            }
        ],
        '30': [
            '30px',
            {
                lineHeight: '34.8px',
                letterSpacing: '-0.9008px'
            }
        ],
        '31': [
            '31px',
            {
                lineHeight: '31px'
            }
        ],
        '40': [
            '40px',
            {
                lineHeight: '40px',
                letterSpacing: '-1.8px'
            }
        ],
        '60': [
            '60px',
            {
                lineHeight: '60px',
                letterSpacing: '-1.8px'
            }
        ],
        '128': [
            '128px',
            {
                lineHeight: '128px',
                letterSpacing: '-1.8px'
            }
        ],
        '192': [
            '192px',
            {
                lineHeight: '153.6px',
                letterSpacing: '-1.8px'
            }
        ],
        '102.4': [
            '102.4px',
            {
                lineHeight: '92.16px'
            }
        ],
        '13.5': [
            '13.5px',
            {
                lineHeight: '17.55px'
            }
        ]
    },
    spacing: {
        '12': '24px',
        '15': '30px',
        '19': '38px',
        '22': '44px',
        '24': '48px',
        '30': '60px',
        '32': '64px',
        '35': '70px',
        '40': '80px',
        '45': '90px',
        '50': '100px',
        '54': '108px',
        '65': '130px',
        '75': '150px',
        '95': '190px',
        '185': '370px',
        '1px': '1px',
        '35px': '35px',
        '55px': '55px',
        '67px': '67px',
        '125px': '125px'
    },
    borderRadius: {
        md: '8px',
        lg: '11px',
        xl: '18px',
        full: '999px'
    },
    boxShadow: {
        sm: 'rgba(0, 0, 0, 0) 0px 0px 0px 0.449482px',
        lg: 'rgba(0, 0, 0, 0.35) 0px 4px 14px 0px',
        xl: 'rgba(0, 0, 0, 0.65) 0px 18px 40px -18px'
    },
    screens: {
        sm: '480px',
        md: '768px',
        lg: '992px',
        xl: '1280px',
        '1440px': '1440px',
        '1920px': '1920px'
    },
    transitionDuration: {
        '300': '0.3s',
        '350': '0.35s',
        '400': '0.4s',
        '500': '0.5s'
    },
    transitionTimingFunction: {
        custom: 'cubic-bezier(0.16, 1, 0.3, 1)'
    },
    container: {
        center: true,
        padding: '15px'
    },
    maxWidth: {
        container: '1630px'
    }
},
  },
};
