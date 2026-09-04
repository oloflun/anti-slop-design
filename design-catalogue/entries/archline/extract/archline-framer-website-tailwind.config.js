/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(45, 100%, 97%)',
            '100': 'hsl(45, 100%, 94%)',
            '200': 'hsl(45, 100%, 86%)',
            '300': 'hsl(45, 100%, 76%)',
            '400': 'hsl(45, 100%, 64%)',
            '500': 'hsl(45, 100%, 50%)',
            '600': 'hsl(45, 100%, 40%)',
            '700': 'hsl(45, 100%, 32%)',
            '800': 'hsl(45, 100%, 24%)',
            '900': 'hsl(45, 100%, 16%)',
            '950': 'hsl(45, 100%, 10%)',
            DEFAULT: '#fffcf3'
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
            '50': 'hsl(21, 24%, 97%)',
            '100': 'hsl(21, 24%, 94%)',
            '200': 'hsl(21, 24%, 86%)',
            '300': 'hsl(21, 24%, 76%)',
            '400': 'hsl(21, 24%, 64%)',
            '500': 'hsl(21, 24%, 50%)',
            '600': 'hsl(21, 24%, 40%)',
            '700': 'hsl(21, 24%, 32%)',
            '800': 'hsl(21, 24%, 24%)',
            '900': 'hsl(21, 24%, 16%)',
            '950': 'hsl(21, 24%, 10%)',
            DEFAULT: '#33261f'
        },
        'neutral-50': '#000000',
        'neutral-100': '#252324',
        background: '#000000',
        foreground: '#000000'
    },
    fontFamily: {
        sans: [
            'Inter Display',
            'sans-serif'
        ],
        body: [
            'Times New Roman',
            'sans-serif'
        ]
    },
    fontSize: {
        '12': [
            '12px',
            {
                lineHeight: 'normal'
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
                lineHeight: 'normal'
            }
        ],
        '28': [
            '28px',
            {
                lineHeight: '39.2px',
                letterSpacing: '-0.2px'
            }
        ],
        '32': [
            '32px',
            {
                lineHeight: '44.8px',
                letterSpacing: '-0.1px'
            }
        ],
        '40': [
            '40px',
            {
                lineHeight: '52px',
                letterSpacing: '-0.1px'
            }
        ],
        '64': [
            '64px',
            {
                lineHeight: 'normal'
            }
        ],
        '72': [
            '72px',
            {
                lineHeight: '82.8px',
                letterSpacing: '-0.3px'
            }
        ],
        '100': [
            '100px',
            {
                lineHeight: '70px',
                letterSpacing: '-0.2px'
            }
        ],
        '18.08': [
            '18.08px',
            {
                lineHeight: '25.312px'
            }
        ],
        '14.08': [
            '14.08px',
            {
                lineHeight: '18.304px'
            }
        ],
        '12.96': [
            '12.96px',
            {
                lineHeight: '16.848px'
            }
        ]
    },
    spacing: {
        '1': '2px',
        '24': '48px',
        '28': '56px',
        '40': '80px',
        '50': '100px',
        '60': '120px',
        '68': '136px',
        '75': '150px',
        '78': '156px',
        '82': '164px',
        '100': '200px',
        '120': '240px'
    },
    borderRadius: {
        sm: '3px',
        md: '8px',
        lg: '11px',
        full: '100px'
    },
    boxShadow: {
        sm: 'rgb(0, 0, 0) 0px 0px 0px 1px inset',
        xs: 'rgba(0, 0, 0, 0.17) 0px 0.602187px 1.56569px -1.5px, rgba(0, 0, 0, 0.14) 0px 2.28853px 5.95019px -3px, rgba(0, 0, 0, 0.02) 0px 10px 26px -4.5px'
    },
    screens: {
        md: '810px'
    },
    transitionDuration: {
        '1': '0.001s'
    },
    container: {
        center: true,
        padding: '0px'
    },
    maxWidth: {
        container: '816px'
    }
},
  },
};
