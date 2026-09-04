/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(1, 81%, 97%)',
            '100': 'hsl(1, 81%, 94%)',
            '200': 'hsl(1, 81%, 86%)',
            '300': 'hsl(1, 81%, 76%)',
            '400': 'hsl(1, 81%, 64%)',
            '500': 'hsl(1, 81%, 50%)',
            '600': 'hsl(1, 81%, 40%)',
            '700': 'hsl(1, 81%, 32%)',
            '800': 'hsl(1, 81%, 24%)',
            '900': 'hsl(1, 81%, 16%)',
            '950': 'hsl(1, 81%, 10%)',
            DEFAULT: '#e82c2a'
        },
        'neutral-50': '#000000',
        'neutral-100': '#212529',
        'neutral-200': '#f2f2f2',
        'neutral-300': '#ffffff',
        'neutral-400': '#121212',
        background: '#ffffff',
        foreground: '#000000'
    },
    fontFamily: {
        sans: [
            'Surt',
            'sans-serif'
        ],
        body: [
            'GTStandard-M',
            'sans-serif'
        ],
        heading: [
            'Editorial Old',
            'sans-serif'
        ]
    },
    fontSize: {
        '0': [
            '0px',
            {
                lineHeight: '0px'
            }
        ],
        '10': [
            '10px',
            {
                lineHeight: 'normal'
            }
        ],
        '15': [
            '15px',
            {
                lineHeight: '22.5px',
                letterSpacing: '0.6px'
            }
        ],
        '20': [
            '20px',
            {
                lineHeight: '24px',
                letterSpacing: '1px'
            }
        ],
        '30': [
            '30px',
            {
                lineHeight: '45px',
                letterSpacing: '0.4px'
            }
        ],
        '35': [
            '35px',
            {
                lineHeight: '52.5px',
                letterSpacing: '0.6px'
            }
        ],
        '60': [
            '60px',
            {
                lineHeight: '108px',
                letterSpacing: '0.6px'
            }
        ],
        '100': [
            '100px',
            {
                lineHeight: '120px',
                letterSpacing: '0.6px'
            }
        ],
        '105': [
            '105px',
            {
                lineHeight: '103.95px',
                letterSpacing: '-0.5px'
            }
        ],
        '150': [
            '150px',
            {
                lineHeight: '165px',
                letterSpacing: '0.6px'
            }
        ]
    },
    spacing: {
        '9': '45px',
        '21': '105px',
        '42': '210px',
        '84': '420px',
        '1px': '1px',
        '64px': '64px'
    },
    borderRadius: {
        sm: '4px',
        full: '50px'
    },
    screens: {
        sm: '600px',
        md: '768px',
        lg: '1024px',
        '1200px': '1200px',
        '1400px': '1400px',
        '1440px': '1440px',
        '1460px': '1460px',
        '2xl': '1600px'
    },
    transitionDuration: {
        '100': '0.1s',
        '150': '0.15s',
        '500': '0.5s'
    },
    transitionTimingFunction: {
        default: 'ease'
    },
    container: {
        center: true,
        padding: '10px'
    },
    maxWidth: {
        container: '100%'
    }
},
  },
};
