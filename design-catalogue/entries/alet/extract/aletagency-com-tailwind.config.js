/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(354, 70%, 97%)',
            '100': 'hsl(354, 70%, 94%)',
            '200': 'hsl(354, 70%, 86%)',
            '300': 'hsl(354, 70%, 76%)',
            '400': 'hsl(354, 70%, 64%)',
            '500': 'hsl(354, 70%, 50%)',
            '600': 'hsl(354, 70%, 40%)',
            '700': 'hsl(354, 70%, 32%)',
            '800': 'hsl(354, 70%, 24%)',
            '900': 'hsl(354, 70%, 16%)',
            '950': 'hsl(354, 70%, 10%)',
            DEFAULT: '#dc3545'
        },
        secondary: {
            '50': 'hsl(45, 39%, 97%)',
            '100': 'hsl(45, 39%, 94%)',
            '200': 'hsl(45, 39%, 86%)',
            '300': 'hsl(45, 39%, 76%)',
            '400': 'hsl(45, 39%, 64%)',
            '500': 'hsl(45, 39%, 50%)',
            '600': 'hsl(45, 39%, 40%)',
            '700': 'hsl(45, 39%, 32%)',
            '800': 'hsl(45, 39%, 24%)',
            '900': 'hsl(45, 39%, 16%)',
            '950': 'hsl(45, 39%, 10%)',
            DEFAULT: '#e5ddc4'
        },
        'neutral-50': '#000000',
        'neutral-100': '#252525',
        'neutral-200': '#101010',
        'neutral-300': '#ffffff',
        'neutral-400': '#454545',
        'neutral-500': '#a2a093',
        'neutral-600': '#bfb5ab',
        background: '#e5ddc4',
        foreground: '#000000'
    },
    fontFamily: {
        body: [
            'SilkSerif-LightItalic',
            'sans-serif'
        ],
        heading: [
            'SilkSerif-Light',
            'sans-serif'
        ]
    },
    fontSize: {
        '12': [
            '12px',
            {
                lineHeight: '13.2px'
            }
        ],
        '36': [
            '36px',
            {
                lineHeight: '33.84px',
                letterSpacing: '1.62px'
            }
        ],
        '20.5632': [
            '20.5632px',
            {
                lineHeight: '19.3294px'
            }
        ],
        '11.52': [
            '11.52px',
            {
                lineHeight: '12.672px'
            }
        ],
        '9.6': [
            '9.6px',
            {
                lineHeight: '11.04px'
            }
        ]
    },
    spacing: {
        '45': '90px',
        '77': '154px',
        '93': '186px',
        '147': '294px',
        '160': '320px',
        '176': '352px',
        '227': '454px',
        '237': '474px',
        '1px': '1px',
        '59px': '59px',
        '237px': '237px',
        '435px': '435px'
    },
    borderRadius: {
        md: '10px',
        full: '9999px'
    },
    boxShadow: {
        sm: 'rgba(0, 0, 0, 0.1) 0px 1px 3px 0px, rgba(0, 0, 0, 0.06) 0px 1px 2px 0px'
    },
    screens: {
        sm: '576px',
        md: '768px',
        lg: '1024px',
        '1200px': '1200px',
        '1400px': '1400px',
        '2xl': '1500px'
    },
    transitionDuration: {
        '200': '0.2s',
        '300': '0.3s',
        '400': '0.4s',
        '1000': '1s',
        '2000': '2s',
        '4000': '4s'
    }
},
  },
};
