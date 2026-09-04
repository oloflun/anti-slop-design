/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(345, 67%, 97%)',
            '100': 'hsl(345, 67%, 94%)',
            '200': 'hsl(345, 67%, 86%)',
            '300': 'hsl(345, 67%, 76%)',
            '400': 'hsl(345, 67%, 64%)',
            '500': 'hsl(345, 67%, 50%)',
            '600': 'hsl(345, 67%, 40%)',
            '700': 'hsl(345, 67%, 32%)',
            '800': 'hsl(345, 67%, 24%)',
            '900': 'hsl(345, 67%, 16%)',
            '950': 'hsl(345, 67%, 10%)',
            DEFAULT: '#fcf0f3'
        },
        secondary: {
            '50': 'hsl(211, 100%, 97%)',
            '100': 'hsl(211, 100%, 94%)',
            '200': 'hsl(211, 100%, 86%)',
            '300': 'hsl(211, 100%, 76%)',
            '400': 'hsl(211, 100%, 64%)',
            '500': 'hsl(211, 100%, 50%)',
            '600': 'hsl(211, 100%, 40%)',
            '700': 'hsl(211, 100%, 32%)',
            '800': 'hsl(211, 100%, 24%)',
            '900': 'hsl(211, 100%, 16%)',
            '950': 'hsl(211, 100%, 10%)',
            DEFAULT: '#007aff'
        },
        accent: {
            '50': 'hsl(358, 100%, 97%)',
            '100': 'hsl(358, 100%, 94%)',
            '200': 'hsl(358, 100%, 86%)',
            '300': 'hsl(358, 100%, 76%)',
            '400': 'hsl(358, 100%, 64%)',
            '500': 'hsl(358, 100%, 50%)',
            '600': 'hsl(358, 100%, 40%)',
            '700': 'hsl(358, 100%, 32%)',
            '800': 'hsl(358, 100%, 24%)',
            '900': 'hsl(358, 100%, 16%)',
            '950': 'hsl(358, 100%, 10%)',
            DEFAULT: '#ff4f55'
        },
        'neutral-50': '#000000',
        'neutral-100': '#ffffff',
        'neutral-200': '#333333',
        'neutral-300': '#808080',
        background: '#ffffff',
        foreground: '#000000'
    },
    fontFamily: {
        sans: [
            'LinotypeHelveticaNeueLTStdRoman',
            'sans-serif'
        ],
        body: [
            'Times New Roman',
            'sans-serif'
        ],
        font2: [
            'Arial',
            'sans-serif'
        ],
        heading: [
            'LinotypeHelveticaNeueLTStdLt',
            'sans-serif'
        ]
    },
    fontSize: {
        '10': [
            '10px',
            {
                lineHeight: '12px'
            }
        ],
        '12': [
            '12px',
            {
                lineHeight: '18px'
            }
        ],
        '14': [
            '14px',
            {
                lineHeight: '28px'
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
                lineHeight: '22px'
            }
        ],
        '28': [
            '28px',
            {
                lineHeight: '31px'
            }
        ],
        '30': [
            '30px',
            {
                lineHeight: '30px'
            }
        ],
        '60': [
            '60px',
            {
                lineHeight: '50px'
            }
        ],
        '90': [
            '90px',
            {
                lineHeight: '80px'
            }
        ],
        '19.2': [
            '19.2px',
            {
                lineHeight: '18px'
            }
        ],
        '13.3333': [
            '13.3333px',
            {
                lineHeight: 'normal'
            }
        ]
    },
    spacing: {
        '15': '30px',
        '20': '40px',
        '26': '52px',
        '30': '60px',
        '40': '80px',
        '50': '100px',
        '75': '150px',
        '163': '326px',
        '191': '382px',
        '240': '480px',
        '1px': '1px',
        '15px': '15px'
    },
    borderRadius: {
        lg: '12px',
        full: '100px'
    },
    screens: {
        xs: '350px',
        sm: '600px',
        md: '782px',
        lg: '992px',
        '1200px': '1200px',
        '1371px': '1371px'
    },
    transitionDuration: {
        '300': '0.3s',
        '350': '0.35s',
        '400': '0.4s',
        '500': '0.5s',
        '600': '0.6s',
        '800': '0.8s'
    },
    transitionTimingFunction: {
        custom: 'cubic-bezier(0.645, 0.045, 0.355, 1)',
        default: 'ease'
    },
    container: {
        center: true,
        padding: '20px'
    },
    maxWidth: {
        container: '100%'
    }
},
  },
};
