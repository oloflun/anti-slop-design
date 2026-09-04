/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(55, 51%, 97%)',
            '100': 'hsl(55, 51%, 94%)',
            '200': 'hsl(55, 51%, 86%)',
            '300': 'hsl(55, 51%, 76%)',
            '400': 'hsl(55, 51%, 64%)',
            '500': 'hsl(55, 51%, 50%)',
            '600': 'hsl(55, 51%, 40%)',
            '700': 'hsl(55, 51%, 32%)',
            '800': 'hsl(55, 51%, 24%)',
            '900': 'hsl(55, 51%, 16%)',
            '950': 'hsl(55, 51%, 10%)',
            DEFAULT: '#efecce'
        },
        secondary: {
            '50': 'hsl(5, 64%, 97%)',
            '100': 'hsl(5, 64%, 94%)',
            '200': 'hsl(5, 64%, 86%)',
            '300': 'hsl(5, 64%, 76%)',
            '400': 'hsl(5, 64%, 64%)',
            '500': 'hsl(5, 64%, 50%)',
            '600': 'hsl(5, 64%, 40%)',
            '700': 'hsl(5, 64%, 32%)',
            '800': 'hsl(5, 64%, 24%)',
            '900': 'hsl(5, 64%, 16%)',
            '950': 'hsl(5, 64%, 10%)',
            DEFAULT: '#b83529'
        },
        accent: {
            '50': 'hsl(54, 47%, 97%)',
            '100': 'hsl(54, 47%, 94%)',
            '200': 'hsl(54, 47%, 86%)',
            '300': 'hsl(54, 47%, 76%)',
            '400': 'hsl(54, 47%, 64%)',
            '500': 'hsl(54, 47%, 50%)',
            '600': 'hsl(54, 47%, 40%)',
            '700': 'hsl(54, 47%, 32%)',
            '800': 'hsl(54, 47%, 24%)',
            '900': 'hsl(54, 47%, 16%)',
            '950': 'hsl(54, 47%, 10%)',
            DEFAULT: '#dcd69d'
        },
        background: '#b83529',
        foreground: '#efecce'
    },
    fontFamily: {
        body: [
            'Flatface Script',
            'sans-serif'
        ],
        heading: [
            'ABC Ginto Nord Condensed',
            'sans-serif'
        ]
    },
    fontSize: {
        '10': [
            '10px',
            {
                lineHeight: '15px'
            }
        ],
        '14': [
            '14px',
            {
                lineHeight: '17.5px',
                letterSpacing: '0.14px'
            }
        ],
        '16': [
            '16px',
            {
                lineHeight: '20px',
                letterSpacing: '-0.16px'
            }
        ],
        '28': [
            '28px',
            {
                lineHeight: '25.2px',
                letterSpacing: '-0.84px'
            }
        ],
        '32': [
            '32px',
            {
                lineHeight: '48px',
                letterSpacing: '0.32px'
            }
        ],
        '36': [
            '36px',
            {
                lineHeight: '32.4px',
                letterSpacing: '-1.08px'
            }
        ],
        '48': [
            '48px',
            {
                lineHeight: '40.8px',
                letterSpacing: '-1.44px'
            }
        ],
        '128': [
            '128px',
            {
                lineHeight: '96px',
                letterSpacing: '-5.12px'
            }
        ]
    },
    spacing: {
        '1': '4px',
        '5': '20px',
        '8': '32px',
        '10': '40px',
        '15': '60px',
        '60': '240px'
    },
    borderRadius: {
        md: '10px',
        xl: '20px',
        full: '50px'
    },
    transitionDuration: {
        '100': '0.1s',
        '150': '0.15s',
        '200': '0.2s',
        '300': '0.3s',
        '500': '0.5s'
    },
    transitionTimingFunction: {
        custom: 'cubic-bezier(0.4, 0, 0.2, 1)',
        linear: 'linear'
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
