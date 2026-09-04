// React Theme — extracted from https://www.happyrobot.ai
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
 *   };
 *   fonts: {
    body: string;
 *   };
 *   fontSizes: {
    '14': string;
    '15': string;
    '16': string;
    '19': string;
    '20': string;
    '21': string;
    '40': string;
    '46': string;
    '76': string;
    '82': string;
    '15.5': string;
    '14.5': string;
 *   };
 *   space: {
    '1': string;
    '40': string;
    '44': string;
    '48': string;
    '56': string;
    '61': string;
    '64': string;
    '72': string;
    '80': string;
    '104': string;
    '120': string;
    '142': string;
    '150': string;
    '160': string;
    '206': string;
 *   };
 *   radii: {
    sm: string;
 *   };
 *   shadows: {
    sm: string;
    xl: string;
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
    "primary": "#b8aea4",
    "secondary": "#fdfcf4",
    "accent": "#12100e",
    "background": "#fdfcf4",
    "foreground": "#000000",
    "neutral50": "#2d2928",
    "neutral100": "#000000",
    "neutral200": "#736f6a",
    "neutral300": "#ece8e3"
  },
  "fonts": {
    "body": "'Tobias', sans-serif"
  },
  "fontSizes": {
    "14": "14px",
    "15": "15px",
    "16": "16px",
    "19": "19px",
    "20": "20px",
    "21": "21px",
    "40": "40px",
    "46": "46px",
    "76": "76px",
    "82": "82px",
    "15.5": "15.5px",
    "14.5": "14.5px"
  },
  "space": {
    "1": "1px",
    "40": "40px",
    "44": "44px",
    "48": "48px",
    "56": "56px",
    "61": "61px",
    "64": "64px",
    "72": "72px",
    "80": "80px",
    "104": "104px",
    "120": "120px",
    "142": "142px",
    "150": "150px",
    "160": "160px",
    "206": "206px"
  },
  "radii": {
    "sm": "3px"
  },
  "shadows": {
    "sm": "rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(184, 174, 164, 0.5) 0px 0px 0px 1px, rgba(0, 0, 0, 0) 0px 0px 0px 0px",
    "xl": "rgba(0, 0, 0, 0.25) 0px 0px 35px 0px"
  },
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
      "main": "#b8aea4",
      "light": "hsl(30, 12%, 83%)",
      "dark": "hsl(30, 12%, 53%)"
    },
    "secondary": {
      "main": "#fdfcf4",
      "light": "hsl(53, 69%, 95%)",
      "dark": "hsl(53, 69%, 82%)"
    },
    "background": {
      "default": "#fdfcf4",
      "paper": "#fcfcfc"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#0e0d0c"
    }
  },
  "typography": {
    "fontFamily": "'Helvetica', sans-serif",
    "h1": {
      "fontSize": "40px",
      "fontWeight": "400",
      "lineHeight": "60px"
    },
    "h3": {
      "fontSize": "20px",
      "fontWeight": "400",
      "lineHeight": "20px"
    }
  },
  "shape": {
    "borderRadius": 3
  },
  "shadows": [
    "rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(184, 174, 164, 0.5) 0px 0px 0px 1px, rgba(0, 0, 0, 0) 0px 0px 0px 0px",
    "rgba(0, 0, 0, 0.25) 0px 0px 35px 0px"
  ]
};

export default theme;
