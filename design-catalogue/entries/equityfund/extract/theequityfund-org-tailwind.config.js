/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(263, 42%, 97%)',
            '100': 'hsl(263, 42%, 94%)',
            '200': 'hsl(263, 42%, 86%)',
            '300': 'hsl(263, 42%, 76%)',
            '400': 'hsl(263, 42%, 64%)',
            '500': 'hsl(263, 42%, 50%)',
            '600': 'hsl(263, 42%, 40%)',
            '700': 'hsl(263, 42%, 32%)',
            '800': 'hsl(263, 42%, 24%)',
            '900': 'hsl(263, 42%, 16%)',
            '950': 'hsl(263, 42%, 10%)',
            DEFAULT: '#c4b3e0'
        },
        secondary: {
            '50': 'hsl(342, 74%, 97%)',
            '100': 'hsl(342, 74%, 94%)',
            '200': 'hsl(342, 74%, 86%)',
            '300': 'hsl(342, 74%, 76%)',
            '400': 'hsl(342, 74%, 64%)',
            '500': 'hsl(342, 74%, 50%)',
            '600': 'hsl(342, 74%, 40%)',
            '700': 'hsl(342, 74%, 32%)',
            '800': 'hsl(342, 74%, 24%)',
            '900': 'hsl(342, 74%, 16%)',
            '950': 'hsl(342, 74%, 10%)',
            DEFAULT: '#500c20'
        },
        accent: {
            '50': 'hsl(36, 71%, 97%)',
            '100': 'hsl(36, 71%, 94%)',
            '200': 'hsl(36, 71%, 86%)',
            '300': 'hsl(36, 71%, 76%)',
            '400': 'hsl(36, 71%, 64%)',
            '500': 'hsl(36, 71%, 50%)',
            '600': 'hsl(36, 71%, 40%)',
            '700': 'hsl(36, 71%, 32%)',
            '800': 'hsl(36, 71%, 24%)',
            '900': 'hsl(36, 71%, 16%)',
            '950': 'hsl(36, 71%, 10%)',
            DEFAULT: '#fcf6ed'
        },
        'neutral-50': '#e5e7eb',
        'neutral-100': '#000000',
        background: '#fcf6ed',
        foreground: '#000000'
    },
    fontFamily: {
        sans: [
            'Metrify Narrow',
            'sans-serif'
        ],
        heading: [
            'Judge',
            'sans-serif'
        ],
        font3: [
            'Metrify',
            'sans-serif'
        ]
    },
    fontSize: {
        '16': [
            '16px',
            {
                lineHeight: '24px'
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
                lineHeight: '28px'
            }
        ],
        '24': [
            '24px',
            {
                lineHeight: '28.8px'
            }
        ],
        '28': [
            '28px',
            {
                lineHeight: '33.6px'
            }
        ],
        '36': [
            '36px',
            {
                lineHeight: '50.4px',
                letterSpacing: '0.36px'
            }
        ],
        '60': [
            '60px',
            {
                lineHeight: '72px'
            }
        ],
        '100': [
            '100px',
            {
                lineHeight: '100px'
            }
        ],
        '204.8': [
            '204.8px',
            {
                lineHeight: '204.8px'
            }
        ],
        '41.6': [
            '41.6px',
            {
                lineHeight: '45.76px',
                letterSpacing: '-0.52px'
            }
        ]
    },
    spacing: {
        '1': '4px',
        '16': '64px',
        '24': '96px',
        '30': '120px',
        '36': '144px',
        '52': '208px',
        '311px': '311px',
        '329px': '329px'
    },
    borderRadius: {
        full: '9999px'
    },
    screens: {
        sm: '640px',
        md: '768px',
        lg: '1024px',
        xl: '1280px',
        '2xl': '1536px'
    },
    transitionDuration: {
        '100': '0.1s',
        '150': '0.15s'
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
