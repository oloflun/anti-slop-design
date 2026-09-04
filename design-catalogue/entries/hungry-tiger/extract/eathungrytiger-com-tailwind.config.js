/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(37, 95%, 97%)',
            '100': 'hsl(37, 95%, 94%)',
            '200': 'hsl(37, 95%, 86%)',
            '300': 'hsl(37, 95%, 76%)',
            '400': 'hsl(37, 95%, 64%)',
            '500': 'hsl(37, 95%, 50%)',
            '600': 'hsl(37, 95%, 40%)',
            '700': 'hsl(37, 95%, 32%)',
            '800': 'hsl(37, 95%, 24%)',
            '900': 'hsl(37, 95%, 16%)',
            '950': 'hsl(37, 95%, 10%)',
            DEFAULT: '#faae33'
        },
        secondary: {
            '50': 'hsl(19, 58%, 97%)',
            '100': 'hsl(19, 58%, 94%)',
            '200': 'hsl(19, 58%, 86%)',
            '300': 'hsl(19, 58%, 76%)',
            '400': 'hsl(19, 58%, 64%)',
            '500': 'hsl(19, 58%, 50%)',
            '600': 'hsl(19, 58%, 40%)',
            '700': 'hsl(19, 58%, 32%)',
            '800': 'hsl(19, 58%, 24%)',
            '900': 'hsl(19, 58%, 16%)',
            '950': 'hsl(19, 58%, 10%)',
            DEFAULT: '#402011'
        },
        accent: {
            '50': 'hsl(0, 100%, 97%)',
            '100': 'hsl(0, 100%, 94%)',
            '200': 'hsl(0, 100%, 86%)',
            '300': 'hsl(0, 100%, 76%)',
            '400': 'hsl(0, 100%, 64%)',
            '500': 'hsl(0, 100%, 50%)',
            '600': 'hsl(0, 100%, 40%)',
            '700': 'hsl(0, 100%, 32%)',
            '800': 'hsl(0, 100%, 24%)',
            '900': 'hsl(0, 100%, 16%)',
            '950': 'hsl(0, 100%, 10%)',
            DEFAULT: '#ffdede'
        },
        'neutral-50': '#000000',
        'neutral-100': '#ffffff',
        'neutral-200': '#dddddd',
        background: '#823513',
        foreground: '#000000'
    },
    fontFamily: {
        sans: [
            'Salmond',
            'sans-serif'
        ],
        body: [
            'Graphikx',
            'sans-serif'
        ]
    },
    fontSize: {
        '64': [
            '64px',
            {
                lineHeight: '57.6px',
                letterSpacing: '-1.28px'
            }
        ],
        '128': [
            '128px',
            {
                lineHeight: '115.2px',
                letterSpacing: '-2.56px'
            }
        ],
        '189.44': [
            '189.44px',
            {
                lineHeight: '151.552px',
                letterSpacing: '-3.7888px'
            }
        ],
        '173.44': [
            '173.44px',
            {
                lineHeight: '173.44px',
                letterSpacing: '-1.7344px'
            }
        ],
        '115.2': [
            '115.2px',
            {
                lineHeight: '103.68px',
                letterSpacing: '-1.8432px'
            }
        ],
        '89.6': [
            '89.6px',
            {
                lineHeight: '78.848px',
                letterSpacing: '-1.4336px'
            }
        ],
        '60.16': [
            '60.16px',
            {
                lineHeight: '55.9488px',
                letterSpacing: '-0.6016px'
            }
        ],
        '57.6': [
            '57.6px',
            {
                lineHeight: '51.84px',
                letterSpacing: '-0.288px'
            }
        ],
        '40.32': [
            '40.32px',
            {
                lineHeight: '36.288px',
                letterSpacing: '-0.8064px'
            }
        ],
        '38.4': [
            '38.4px',
            {
                lineHeight: '26.88px',
                letterSpacing: '-0.384px'
            }
        ],
        '37.12': [
            '37.12px',
            {
                lineHeight: '35.264px',
                letterSpacing: '-0.3712px'
            }
        ],
        '35.84': [
            '35.84px',
            {
                lineHeight: '35.84px',
                letterSpacing: '-0.7168px'
            }
        ],
        '27.52': [
            '27.52px',
            {
                lineHeight: '24.768px',
                letterSpacing: '-0.5504px'
            }
        ],
        '25.6': [
            '25.6px',
            {
                lineHeight: '25.6px',
                letterSpacing: '-0.256px'
            }
        ],
        '19.2': [
            '19.2px',
            {
                lineHeight: '26.88px'
            }
        ]
    },
    spacing: {
        '14': '28px',
        '21': '42px',
        '50': '100px',
        '56': '112px',
        '61': '122px',
        '64': '128px',
        '77': '154px',
        '86': '172px',
        '89': '178px',
        '96': '192px',
        '128': '256px',
        '136': '272px',
        '148': '296px',
        '153': '306px',
        '224': '448px',
        '1px': '1px',
        '23px': '23px',
        '51px': '51px',
        '61px': '61px',
        '245px': '245px'
    },
    borderRadius: {
        sm: '5px',
        md: '8px',
        lg: '12px',
        full: '1280px'
    },
    screens: {
        md: '768px'
    },
    transitionDuration: {
        '400': '0.4s',
        '450': '0.45s',
        '600': '0.6s',
        '1500': '1.5s'
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
