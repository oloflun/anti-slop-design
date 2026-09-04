/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(65, 12%, 97%)',
            '100': 'hsl(65, 12%, 94%)',
            '200': 'hsl(65, 12%, 86%)',
            '300': 'hsl(65, 12%, 76%)',
            '400': 'hsl(65, 12%, 64%)',
            '500': 'hsl(65, 12%, 50%)',
            '600': 'hsl(65, 12%, 40%)',
            '700': 'hsl(65, 12%, 32%)',
            '800': 'hsl(65, 12%, 24%)',
            '900': 'hsl(65, 12%, 16%)',
            '950': 'hsl(65, 12%, 10%)',
            DEFAULT: '#62644e'
        },
        secondary: {
            '50': 'hsl(46, 33%, 97%)',
            '100': 'hsl(46, 33%, 94%)',
            '200': 'hsl(46, 33%, 86%)',
            '300': 'hsl(46, 33%, 76%)',
            '400': 'hsl(46, 33%, 64%)',
            '500': 'hsl(46, 33%, 50%)',
            '600': 'hsl(46, 33%, 40%)',
            '700': 'hsl(46, 33%, 32%)',
            '800': 'hsl(46, 33%, 24%)',
            '900': 'hsl(46, 33%, 16%)',
            '950': 'hsl(46, 33%, 10%)',
            DEFAULT: '#f2efe5'
        },
        accent: {
            '50': 'hsl(45, 32%, 97%)',
            '100': 'hsl(45, 32%, 94%)',
            '200': 'hsl(45, 32%, 86%)',
            '300': 'hsl(45, 32%, 76%)',
            '400': 'hsl(45, 32%, 64%)',
            '500': 'hsl(45, 32%, 50%)',
            '600': 'hsl(45, 32%, 40%)',
            '700': 'hsl(45, 32%, 32%)',
            '800': 'hsl(45, 32%, 24%)',
            '900': 'hsl(45, 32%, 16%)',
            '950': 'hsl(45, 32%, 10%)',
            DEFAULT: '#e6e0ce'
        },
        'neutral-50': '#000000',
        'neutral-100': '#2b2927',
        'neutral-200': '#736e6a',
        'neutral-300': '#ffffff',
        'neutral-400': '#5c7c68',
        'neutral-500': '#a89e95',
        background: '#f2efe5',
        foreground: '#000000'
    },
    fontFamily: {
        body: [
            'Manrope',
            'sans-serif'
        ]
    },
    fontSize: {
        '10': [
            '10px',
            {
                lineHeight: '11px'
            }
        ],
        '12': [
            '12px',
            {
                lineHeight: 'normal'
            }
        ],
        '13': [
            '13px',
            {
                lineHeight: '15.6px'
            }
        ],
        '14': [
            '14px',
            {
                lineHeight: '18.2px'
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
        '17': [
            '17px',
            {
                lineHeight: '20.4px'
            }
        ],
        '18': [
            '18px',
            {
                lineHeight: '23.4px',
                letterSpacing: '-0.18px'
            }
        ],
        '20': [
            '20px',
            {
                lineHeight: '24px'
            }
        ],
        '36': [
            '36px',
            {
                lineHeight: '39.6px'
            }
        ],
        '64': [
            '64px',
            {
                lineHeight: '64px'
            }
        ],
        '69': [
            '69px',
            {
                lineHeight: '69px',
                letterSpacing: '-2.07px'
            }
        ],
        '73': [
            '73px',
            {
                lineHeight: '73px',
                letterSpacing: '-2.19px'
            }
        ],
        '75': [
            '75px',
            {
                lineHeight: '75px',
                letterSpacing: '-2.25px'
            }
        ],
        '96': [
            '96px',
            {
                lineHeight: '105.6px'
            }
        ]
    },
    spacing: {
        '2': '4px',
        '15': '30px',
        '20': '40px',
        '25': '50px',
        '28': '56px',
        '30': '60px',
        '36': '72px',
        '40': '80px',
        '45': '90px',
        '60': '120px',
        '80': '160px',
        '19px': '19px',
        '103px': '103px'
    },
    borderRadius: {
        sm: '3px',
        md: '8px',
        lg: '16px',
        xl: '20px',
        full: '100px'
    },
    transitionDuration: {
        '1': '0.001s'
    },
    container: {
        center: true,
        padding: '20px'
    },
    maxWidth: {
        container: '1600px'
    }
},
  },
};
