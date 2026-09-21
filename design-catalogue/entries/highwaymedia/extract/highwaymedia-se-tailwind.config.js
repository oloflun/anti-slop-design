/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(318, 21%, 97%)',
            '100': 'hsl(318, 21%, 94%)',
            '200': 'hsl(318, 21%, 86%)',
            '300': 'hsl(318, 21%, 76%)',
            '400': 'hsl(318, 21%, 64%)',
            '500': 'hsl(318, 21%, 50%)',
            '600': 'hsl(318, 21%, 40%)',
            '700': 'hsl(318, 21%, 32%)',
            '800': 'hsl(318, 21%, 24%)',
            '900': 'hsl(318, 21%, 16%)',
            '950': 'hsl(318, 21%, 10%)',
            DEFAULT: '#624058'
        },
        secondary: {
            '50': 'hsl(345, 72%, 97%)',
            '100': 'hsl(345, 72%, 94%)',
            '200': 'hsl(345, 72%, 86%)',
            '300': 'hsl(345, 72%, 76%)',
            '400': 'hsl(345, 72%, 64%)',
            '500': 'hsl(345, 72%, 50%)',
            '600': 'hsl(345, 72%, 40%)',
            '700': 'hsl(345, 72%, 32%)',
            '800': 'hsl(345, 72%, 24%)',
            '900': 'hsl(345, 72%, 16%)',
            '950': 'hsl(345, 72%, 10%)',
            DEFAULT: '#ec8aa3'
        },
        accent: {
            '50': 'hsl(134, 41%, 97%)',
            '100': 'hsl(134, 41%, 94%)',
            '200': 'hsl(134, 41%, 86%)',
            '300': 'hsl(134, 41%, 76%)',
            '400': 'hsl(134, 41%, 64%)',
            '500': 'hsl(134, 41%, 50%)',
            '600': 'hsl(134, 41%, 40%)',
            '700': 'hsl(134, 41%, 32%)',
            '800': 'hsl(134, 41%, 24%)',
            '900': 'hsl(134, 41%, 16%)',
            '950': 'hsl(134, 41%, 10%)',
            DEFAULT: '#d4edda'
        },
        'neutral-50': '#232323',
        'neutral-100': '#000000',
        'neutral-200': '#ffffff',
        'neutral-300': '#495057',
        'neutral-400': '#929292',
        'neutral-500': '#656565',
        'neutral-600': '#dee2e6',
        'neutral-700': '#cccccc',
        'neutral-800': '#333333',
        'neutral-900': '#ffe8ee',
        background: '#ffffff',
        foreground: '#000000'
    },
    fontFamily: {
        body: [
            'Open Sans',
            'sans-serif'
        ],
        heading: [
            'Outfit',
            'sans-serif'
        ]
    },
    fontSize: {
        '16': [
            '16px',
            {
                lineHeight: '18.4px'
            }
        ],
        '18': [
            '18px',
            {
                lineHeight: '27px'
            }
        ],
        '20': [
            '20px',
            {
                lineHeight: '30px'
            }
        ],
        '22': [
            '22px',
            {
                lineHeight: '22px'
            }
        ],
        '24': [
            '24px',
            {
                lineHeight: '36px'
            }
        ],
        '26': [
            '26px',
            {
                lineHeight: '39px'
            }
        ],
        '30': [
            '30px',
            {
                lineHeight: '45px'
            }
        ],
        '34': [
            '34px',
            {
                lineHeight: '40.8px'
            }
        ],
        '42': [
            '42px',
            {
                lineHeight: '50.4px'
            }
        ],
        '54': [
            '54px',
            {
                lineHeight: '64.8px'
            }
        ],
        '56': [
            '56px',
            {
                lineHeight: '60px'
            }
        ],
        '60': [
            '60px',
            {
                lineHeight: '90px'
            }
        ],
        '84': [
            '84px',
            {
                lineHeight: '100.8px'
            }
        ],
        '102.4': [
            '102.4px',
            {
                lineHeight: '153.6px'
            }
        ],
        '25.6': [
            '25.6px',
            {
                lineHeight: '30.72px'
            }
        ]
    },
    spacing: {
        '0': '0px',
        '4': '20px',
        '5': '25px',
        '8': '40px',
        '9': '45px',
        '10': '50px',
        '12': '60px',
        '14': '70px',
        '20': '100px',
        '24': '120px',
        '28': '140px',
        '40': '200px',
        '48': '240px',
        '77': '385px',
        '28px': '28px',
        '73px': '73px',
        '106px': '106px'
    },
    borderRadius: {
        sm: '3px',
        md: '10px',
        lg: '15px',
        xl: '20px',
        full: '100px'
    },
    boxShadow: {
        lg: 'rgba(0, 0, 0, 0.1) 0px 0px 29px -4px'
    },
    screens: {
        md: '768px',
        lg: '992px',
        '1200px': '1200px',
        '1400px': '1400px',
        '2xl': '1600px',
        '1900px': '1900px',
        '1920px': '1920px',
        '2300px': '2300px'
    },
    transitionDuration: {
        '1': '0.001s',
        '100': '0.1s',
        '150': '0.15s',
        '200': '0.2s',
        '300': '0.3s',
        '400': '0.4s',
        '600': '0.6s',
        '800': '0.8s',
        '1000': '1s',
        '1200': '1.2s'
    },
    transitionTimingFunction: {
        default: 'ease',
        custom: 'cubic-bezier(0.445, 0.05, 0.55, 0.95)'
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
