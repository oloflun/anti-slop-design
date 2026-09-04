/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(240, 17%, 97%)',
            '100': 'hsl(240, 17%, 94%)',
            '200': 'hsl(240, 17%, 86%)',
            '300': 'hsl(240, 17%, 76%)',
            '400': 'hsl(240, 17%, 64%)',
            '500': 'hsl(240, 17%, 50%)',
            '600': 'hsl(240, 17%, 40%)',
            '700': 'hsl(240, 17%, 32%)',
            '800': 'hsl(240, 17%, 24%)',
            '900': 'hsl(240, 17%, 16%)',
            '950': 'hsl(240, 17%, 10%)',
            DEFAULT: '#111118'
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
            '50': 'hsl(52, 98%, 97%)',
            '100': 'hsl(52, 98%, 94%)',
            '200': 'hsl(52, 98%, 86%)',
            '300': 'hsl(52, 98%, 76%)',
            '400': 'hsl(52, 98%, 64%)',
            '500': 'hsl(52, 98%, 50%)',
            '600': 'hsl(52, 98%, 40%)',
            '700': 'hsl(52, 98%, 32%)',
            '800': 'hsl(52, 98%, 24%)',
            '900': 'hsl(52, 98%, 16%)',
            '950': 'hsl(52, 98%, 10%)',
            DEFAULT: '#fef199'
        },
        'neutral-50': '#ffffff',
        'neutral-100': '#000000',
        'neutral-200': '#222222',
        'neutral-300': '#333333',
        'neutral-400': '#7c7c7c',
        'neutral-500': '#445567',
        'neutral-600': '#dddddd',
        background: '#ffffff',
        foreground: '#000000'
    },
    fontFamily: {
        sans: [
            'PP Mori',
            'sans-serif'
        ],
        heading: [
            'Editorial New',
            'sans-serif'
        ],
        body: [
            'webflow-icons',
            'sans-serif'
        ]
    },
    fontSize: {
        '12': [
            '12px',
            {
                lineHeight: '12px'
            }
        ],
        '14': [
            '14px',
            {
                lineHeight: '19.6px'
            }
        ],
        '15': [
            '15px',
            {
                lineHeight: '18px'
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
                lineHeight: '21.6px'
            }
        ],
        '24': [
            '24px',
            {
                lineHeight: '28.8px'
            }
        ],
        '40': [
            '40px',
            {
                lineHeight: '48px'
            }
        ],
        '48': [
            '48px',
            {
                lineHeight: '57.6px'
            }
        ],
        '72': [
            '72px',
            {
                lineHeight: '72px'
            }
        ],
        '160': [
            '160px',
            {
                lineHeight: '176px'
            }
        ],
        '70.4': [
            '70.4px',
            {
                lineHeight: '77.44px'
            }
        ],
        '12.8': [
            '12.8px',
            {
                lineHeight: '15.36px'
            }
        ]
    },
    spacing: {
        '15': '30px',
        '20': '40px',
        '30': '60px',
        '40': '80px',
        '56': '112px',
        '70': '140px',
        '85': '170px',
        '3px': '3px'
    },
    borderRadius: {
        md: '8px',
        xl: '24px',
        full: '800px'
    },
    boxShadow: {
        xs: 'rgba(51, 51, 51, 0.4) 0px 0px 3px 0px'
    },
    screens: {
        md: '768px'
    },
    transitionDuration: {
        '100': '0.1s',
        '200': '0.2s',
        '300': '0.3s',
        '400': '0.4s'
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
