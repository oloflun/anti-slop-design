// React Theme — extracted from https://vestris.ai/
// Compatible with: Chakra UI, Stitches, Vanilla Extract, or any CSS-in-JS

/**
 * TypeScript type definition for this theme:
 *
 * interface Theme {
 *   colors: {
    primary: string;
    secondary: string;
    accent: string;
    background: string;
    foreground: string;
    neutral50: string;
    neutral100: string;
    neutral200: string;
    neutral300: string;
    neutral400: string;
    neutral500: string;
 *   };
 *   fonts: {
    body: string;
 *   };
 *   fontSizes: {
    '14': string;
    '15': string;
    '16': string;
    '17': string;
    '18': string;
    '20': string;
    '36': string;
    '64': string;
    '69': string;
    '73': string;
    '75': string;
    '96': string;
 *   };
 *   space: {
    '4': string;
    '19': string;
    '30': string;
    '40': string;
    '50': string;
    '56': string;
    '60': string;
    '72': string;
    '80': string;
    '90': string;
    '103': string;
    '120': string;
    '160': string;
 *   };
 *   radii: {
    sm: string;
    md: string;
    lg: string;
    xl: string;
    full: string;
 *   };
 *   shadows: {

 *   };
 *   states: {
 *     hover: { opacity: number };
 *     focus: { opacity: number };
 *     active: { opacity: number };
 *     disabled: { opacity: number };
 *   };
 * }
 */

export const theme = {
  "colors": {
    "primary": "#62644e",
    "secondary": "#f2efe5",
    "accent": "#e6e0ce",
    "background": "#f2efe5",
    "foreground": "#000000",
    "neutral50": "#000000",
    "neutral100": "#2b2927",
    "neutral200": "#736e6a",
    "neutral300": "#ffffff",
    "neutral400": "#5c7c68",
    "neutral500": "#a89e95"
  },
  "fonts": {
    "body": "'Manrope', sans-serif"
  },
  "fontSizes": {
    "14": "14px",
    "15": "15px",
    "16": "16px",
    "17": "17px",
    "18": "18px",
    "20": "20px",
    "36": "36px",
    "64": "64px",
    "69": "69px",
    "73": "73px",
    "75": "75px",
    "96": "96px"
  },
  "space": {
    "4": "4px",
    "19": "19px",
    "30": "30px",
    "40": "40px",
    "50": "50px",
    "56": "56px",
    "60": "60px",
    "72": "72px",
    "80": "80px",
    "90": "90px",
    "103": "103px",
    "120": "120px",
    "160": "160px"
  },
  "radii": {
    "sm": "3px",
    "md": "8px",
    "lg": "16px",
    "xl": "20px",
    "full": "100px"
  },
  "shadows": {},
  "states": {
    "hover": {
      "opacity": 0.08
    },
    "focus": {
      "opacity": 0.12
    },
    "active": {
      "opacity": 0.16
    },
    "disabled": {
      "opacity": 0.38
    }
  }
};

// MUI v5 theme
export const muiTheme = {
  "palette": {
    "primary": {
      "main": "#62644e",
      "light": "hsl(65, 12%, 50%)",
      "dark": "hsl(65, 12%, 20%)"
    },
    "secondary": {
      "main": "#f2efe5",
      "light": "hsl(46, 33%, 95%)",
      "dark": "hsl(46, 33%, 77%)"
    },
    "background": {
      "default": "#f2efe5",
      "paper": "#ffffff"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#0000ee"
    }
  },
  "typography": {
    "fontFamily": "'Instrument Serif', sans-serif",
    "h1": {
      "fontSize": "36px",
      "fontWeight": "400",
      "lineHeight": "39.6px"
    }
  },
  "shape": {
    "borderRadius": 8
  },
  "shadows": []
};

export default theme;
