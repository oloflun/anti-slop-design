/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(208, 83%, 97%)',
            '100': 'hsl(208, 83%, 94%)',
            '200': 'hsl(208, 83%, 86%)',
            '300': 'hsl(208, 83%, 76%)',
            '400': 'hsl(208, 83%, 64%)',
            '500': 'hsl(208, 83%, 50%)',
            '600': 'hsl(208, 83%, 40%)',
            '700': 'hsl(208, 83%, 32%)',
            '800': 'hsl(208, 83%, 24%)',
            '900': 'hsl(208, 83%, 16%)',
            '950': 'hsl(208, 83%, 10%)',
            DEFAULT: '#3898ec'
        },
        secondary: {
            '50': 'hsl(278, 67%, 97%)',
            '100': 'hsl(278, 67%, 94%)',
            '200': 'hsl(278, 67%, 86%)',
            '300': 'hsl(278, 67%, 76%)',
            '400': 'hsl(278, 67%, 64%)',
            '500': 'hsl(278, 67%, 50%)',
            '600': 'hsl(278, 67%, 40%)',
            '700': 'hsl(278, 67%, 32%)',
            '800': 'hsl(278, 67%, 24%)',
            '900': 'hsl(278, 67%, 16%)',
            '950': 'hsl(278, 67%, 10%)',
            DEFAULT: '#07020a'
        },
        accent: {
            '50': 'hsl(200, 100%, 97%)',
            '100': 'hsl(200, 100%, 94%)',
            '200': 'hsl(200, 100%, 86%)',
            '300': 'hsl(200, 100%, 76%)',
            '400': 'hsl(200, 100%, 64%)',
            '500': 'hsl(200, 100%, 50%)',
            '600': 'hsl(200, 100%, 40%)',
            '700': 'hsl(200, 100%, 32%)',
            '800': 'hsl(200, 100%, 24%)',
            '900': 'hsl(200, 100%, 16%)',
            '950': 'hsl(200, 100%, 10%)',
            DEFAULT: '#6ccfff'
        },
        'neutral-50': '#ffffff',
        'neutral-100': '#333333',
        'neutral-200': '#cccccc',
        background: '#07020a',
        foreground: '#000000'
    },
    fontFamily: {
        sans: [
            'RRE Monument Grotesk Trial',
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
                lineHeight: '16.8px'
            }
        ],
        '15': [
            '15px',
            {
                lineHeight: '21px'
            }
        ],
        '16': [
            '16px',
            {
                lineHeight: 'normal'
            }
        ],
        '20': [
            '20px',
            {
                lineHeight: '28px'
            }
        ],
        '24': [
            '24px',
            {
                lineHeight: '33.6px'
            }
        ],
        '32': [
            '32px',
            {
                lineHeight: '38.4px'
            }
        ],
        '56': [
            '56px',
            {
                lineHeight: '56px',
                letterSpacing: '-2px'
            }
        ],
        '80': [
            '80px',
            {
                lineHeight: '88px',
                letterSpacing: '-4px'
            }
        ]
    },
    spacing: {
        '24': '48px',
        '39': '78px',
        '48': '96px',
        '64': '128px',
        '100': '200px',
        '1px': '1px'
    },
    screens: {
        md: '768px',
        lg: '991px',
        '2xl': '1520px'
    },
    transitionDuration: {
        '200': '0.2s',
        '300': '0.3s',
        '400': '0.4s'
    },
    transitionTimingFunction: {
        custom: 'cubic-bezier(0.25, 1, 0.5, 1)'
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
