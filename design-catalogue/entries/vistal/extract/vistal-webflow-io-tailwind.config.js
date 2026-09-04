/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(62, 90%, 97%)',
            '100': 'hsl(62, 90%, 94%)',
            '200': 'hsl(62, 90%, 86%)',
            '300': 'hsl(62, 90%, 76%)',
            '400': 'hsl(62, 90%, 64%)',
            '500': 'hsl(62, 90%, 50%)',
            '600': 'hsl(62, 90%, 40%)',
            '700': 'hsl(62, 90%, 32%)',
            '800': 'hsl(62, 90%, 24%)',
            '900': 'hsl(62, 90%, 16%)',
            '950': 'hsl(62, 90%, 10%)',
            DEFAULT: '#ebf213'
        },
        secondary: {
            '50': 'hsl(274, 100%, 97%)',
            '100': 'hsl(274, 100%, 94%)',
            '200': 'hsl(274, 100%, 86%)',
            '300': 'hsl(274, 100%, 76%)',
            '400': 'hsl(274, 100%, 64%)',
            '500': 'hsl(274, 100%, 50%)',
            '600': 'hsl(274, 100%, 40%)',
            '700': 'hsl(274, 100%, 32%)',
            '800': 'hsl(274, 100%, 24%)',
            '900': 'hsl(274, 100%, 16%)',
            '950': 'hsl(274, 100%, 10%)',
            DEFAULT: '#8f00ff'
        },
        accent: {
            '50': 'hsl(50, 83%, 97%)',
            '100': 'hsl(50, 83%, 94%)',
            '200': 'hsl(50, 83%, 86%)',
            '300': 'hsl(50, 83%, 76%)',
            '400': 'hsl(50, 83%, 64%)',
            '500': 'hsl(50, 83%, 50%)',
            '600': 'hsl(50, 83%, 40%)',
            '700': 'hsl(50, 83%, 32%)',
            '800': 'hsl(50, 83%, 24%)',
            '900': 'hsl(50, 83%, 16%)',
            '950': 'hsl(50, 83%, 10%)',
            DEFAULT: '#efd556'
        },
        'neutral-50': '#000000',
        'neutral-100': '#ffffff',
        'neutral-200': '#656565',
        'neutral-300': '#131313',
        'neutral-400': '#333333',
        'neutral-500': '#f0efed',
        'neutral-600': '#bababa',
        'neutral-700': '#c8c8c8',
        background: '#ffffff',
        foreground: '#000000'
    },
    fontFamily: {
        sans: [
            'Inter',
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
                lineHeight: '18px',
                letterSpacing: '-0.36px'
            }
        ],
        '14': [
            '14px',
            {
                lineHeight: '20px',
                letterSpacing: '0.28px'
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
                lineHeight: '36px',
                letterSpacing: '0.32px'
            }
        ],
        '40': [
            '40px',
            {
                lineHeight: '48px',
                letterSpacing: '-1.2px'
            }
        ],
        '48': [
            '48px',
            {
                lineHeight: '52.8px',
                letterSpacing: '-1.92px'
            }
        ],
        '64': [
            '64px',
            {
                lineHeight: '70.4px',
                letterSpacing: '-2.56px'
            }
        ],
        '72': [
            '72px',
            {
                lineHeight: '79.2px',
                letterSpacing: '-2.88px'
            }
        ],
        '80': [
            '80px',
            {
                lineHeight: '88px',
                letterSpacing: '-3.2px'
            }
        ]
    },
    spacing: {
        '1': '2px',
        '16': '32px',
        '20': '40px',
        '30': '60px',
        '36': '72px',
        '60': '120px',
        '120': '240px',
        '149': '298px',
        '166': '332px',
        '95px': '95px',
        '109px': '109px',
        '247px': '247px'
    },
    borderRadius: {
        xs: '2px',
        md: '8px',
        lg: '12px',
        xl: '24px',
        full: '100px'
    },
    boxShadow: {
        xl: 'rgba(0, 0, 0, 0.1) 0px 14px 32px 0px, rgba(0, 0, 0, 0.09) 0px 58px 58px 0px, rgba(0, 0, 0, 0.05) 0px 130px 78px 0px, rgba(0, 0, 0, 0.01) 0px 232px 93px 0px, rgba(0, 0, 0, 0) 0px 362px 101px 0px'
    },
    screens: {
        md: '768px'
    },
    transitionDuration: {
        '100': '0.1s',
        '200': '0.2s',
        '300': '0.3s'
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
        container: '1320px'
    }
},
  },
};
