/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(45, 92%, 97%)',
            '100': 'hsl(45, 92%, 94%)',
            '200': 'hsl(45, 92%, 86%)',
            '300': 'hsl(45, 92%, 76%)',
            '400': 'hsl(45, 92%, 64%)',
            '500': 'hsl(45, 92%, 50%)',
            '600': 'hsl(45, 92%, 40%)',
            '700': 'hsl(45, 92%, 32%)',
            '800': 'hsl(45, 92%, 24%)',
            '900': 'hsl(45, 92%, 16%)',
            '950': 'hsl(45, 92%, 10%)',
            DEFAULT: '#fcecba'
        },
        secondary: {
            '50': 'hsl(260, 66%, 97%)',
            '100': 'hsl(260, 66%, 94%)',
            '200': 'hsl(260, 66%, 86%)',
            '300': 'hsl(260, 66%, 76%)',
            '400': 'hsl(260, 66%, 64%)',
            '500': 'hsl(260, 66%, 50%)',
            '600': 'hsl(260, 66%, 40%)',
            '700': 'hsl(260, 66%, 32%)',
            '800': 'hsl(260, 66%, 24%)',
            '900': 'hsl(260, 66%, 16%)',
            '950': 'hsl(260, 66%, 10%)',
            DEFAULT: '#5124ae'
        },
        'neutral-50': '#e5e7eb',
        'neutral-100': '#000000',
        background: '#5124ae',
        foreground: '#000000'
    },
    fontFamily: {
        sans: [
            'Circular',
            'sans-serif'
        ],
        body: [
            'Times New Roman',
            'sans-serif'
        ]
    },
    fontSize: {
        '14': [
            '14px',
            {
                lineHeight: '23.8px',
                letterSpacing: '1.4px'
            }
        ],
        '16': [
            '16px',
            {
                lineHeight: '24px'
            }
        ],
        '22': [
            '22px',
            {
                lineHeight: '30.8px'
            }
        ],
        '32': [
            '32px',
            {
                lineHeight: '44.8px',
                letterSpacing: '-0.32px'
            }
        ],
        '48': [
            '48px',
            {
                lineHeight: '45.6px',
                letterSpacing: '-0.48px'
            }
        ],
        '88': [
            '88px',
            {
                lineHeight: '96.8px',
                letterSpacing: '-1.76px'
            }
        ],
        '132': [
            '132px',
            {
                lineHeight: '125.4px',
                letterSpacing: '-2.64px'
            }
        ]
    },
    spacing: {
        '0': '0px',
        '16': '64px',
        '24': '96px',
        '30': '120px',
        '40': '160px',
        '48': '192px'
    },
    borderRadius: {
        xs: '2px',
        full: '9999px'
    },
    boxShadow: {
        sm: 'rgb(255, 255, 255) 0px 0px 0px 0px, rgba(59, 130, 246, 0.5) 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 10px 15px -3px, rgba(0, 0, 0, 0.1) 0px 4px 6px -4px'
    },
    screens: {
        sm: '480px',
        md: '768px',
        lg: '976px',
        '1440px': '1440px',
        '2xl': '1600px',
        '1920px': '1920px'
    },
    transitionDuration: {
        '150': '0.15s',
        '200': '0.2s',
        '300': '0.3s',
        '400': '0.4s',
        '500': '0.5s',
        '700': '0.7s'
    },
    transitionTimingFunction: {
        custom: 'cubic-bezier(0.4, 0, 0.2, 1)'
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
