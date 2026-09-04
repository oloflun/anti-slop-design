/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(61, 84%, 97%)',
            '100': 'hsl(61, 84%, 94%)',
            '200': 'hsl(61, 84%, 86%)',
            '300': 'hsl(61, 84%, 76%)',
            '400': 'hsl(61, 84%, 64%)',
            '500': 'hsl(61, 84%, 50%)',
            '600': 'hsl(61, 84%, 40%)',
            '700': 'hsl(61, 84%, 32%)',
            '800': 'hsl(61, 84%, 24%)',
            '900': 'hsl(61, 84%, 16%)',
            '950': 'hsl(61, 84%, 10%)',
            DEFAULT: '#f8f9b8'
        },
        secondary: {
            '50': 'hsl(60, 11%, 97%)',
            '100': 'hsl(60, 11%, 94%)',
            '200': 'hsl(60, 11%, 86%)',
            '300': 'hsl(60, 11%, 76%)',
            '400': 'hsl(60, 11%, 64%)',
            '500': 'hsl(60, 11%, 50%)',
            '600': 'hsl(60, 11%, 40%)',
            '700': 'hsl(60, 11%, 32%)',
            '800': 'hsl(60, 11%, 24%)',
            '900': 'hsl(60, 11%, 16%)',
            '950': 'hsl(60, 11%, 10%)',
            DEFAULT: '#f7f7f5'
        },
        accent: {
            '50': 'hsl(20, 98%, 97%)',
            '100': 'hsl(20, 98%, 94%)',
            '200': 'hsl(20, 98%, 86%)',
            '300': 'hsl(20, 98%, 76%)',
            '400': 'hsl(20, 98%, 64%)',
            '500': 'hsl(20, 98%, 50%)',
            '600': 'hsl(20, 98%, 40%)',
            '700': 'hsl(20, 98%, 32%)',
            '800': 'hsl(20, 98%, 24%)',
            '900': 'hsl(20, 98%, 16%)',
            '950': 'hsl(20, 98%, 10%)',
            DEFAULT: '#fd8143'
        },
        'neutral-50': '#000000',
        'neutral-100': '#22201f',
        'neutral-200': '#777777',
        'neutral-300': '#ffffff',
        'neutral-400': '#646464',
        'neutral-500': '#d8d7d3',
        'neutral-600': '#0f0e0e',
        'neutral-700': '#eeedeb',
        'neutral-800': '#e0e0e0',
        'neutral-900': '#555555',
        background: '#ffffff',
        foreground: '#000000'
    },
    fontFamily: {
        body: [
            'Arial',
            'sans-serif'
        ],
        heading: [
            'FigtreeKH',
            'sans-serif'
        ],
        font4: [
            'Affairs',
            'sans-serif'
        ]
    },
    fontSize: {
        '12': [
            '12px',
            {
                lineHeight: '12px'
            }
        ],
        '13': [
            '13px',
            {
                lineHeight: '19.5px'
            }
        ],
        '14': [
            '14px',
            {
                lineHeight: '16.8px'
            }
        ],
        '15': [
            '15px',
            {
                lineHeight: '22.5px'
            }
        ],
        '16': [
            '16px',
            {
                lineHeight: 'normal'
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
                lineHeight: '30px'
            }
        ],
        '24': [
            '24px',
            {
                lineHeight: '0px',
                letterSpacing: '-0.65px'
            }
        ],
        '32': [
            '32px',
            {
                lineHeight: '38.4px',
                letterSpacing: '-0.65px'
            }
        ],
        '40': [
            '40px',
            {
                lineHeight: '48px',
                letterSpacing: '-0.75px'
            }
        ],
        '44': [
            '44px',
            {
                lineHeight: '44px',
                letterSpacing: '-0.5px'
            }
        ],
        '48': [
            '48px',
            {
                lineHeight: '52.8px',
                letterSpacing: '-1.5px'
            }
        ],
        '72': [
            '72px',
            {
                lineHeight: '79.2px',
                letterSpacing: '-2px'
            }
        ],
        '96': [
            '96px',
            {
                lineHeight: '96px',
                letterSpacing: '-1.5px'
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
        '0': '1px',
        '1': '24px',
        '2': '30px',
        '3': '39px',
        '4': '48px',
        '5': '63px',
        '6': '69px',
        '7': '80px',
        '8': '120px',
        '9': '144px',
        '10': '187px',
        '11': '245px'
    },
    borderRadius: {
        sm: '4px',
        md: '8px',
        lg: '12px',
        full: '900px'
    },
    boxShadow: {
        xl: 'rgba(0, 0, 0, 0.15) 0px 8px 32px 0px'
    },
    transitionDuration: {
        '200': '0.2s',
        '250': '0.25s',
        '300': '0.3s'
    },
    container: {
        center: true,
        padding: '0px'
    },
    maxWidth: {
        container: '1400px'
    }
},
  },
};
