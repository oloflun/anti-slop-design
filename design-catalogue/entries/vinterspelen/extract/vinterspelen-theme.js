// React Theme — extracted from http://127.0.0.1:3055/sites/vinterspelen.html
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
    '16': string;
    '18': string;
    '19': string;
    '21': string;
    '23': string;
    '64': string;
    '101.12': string;
    '81.92': string;
    '44.8': string;
    '39.04': string;
    '24.32': string;
    '15.5': string;
 *   };
 *   space: {
    '2': string;
    '56': string;
    '64': string;
    '80': string;
    '96': string;
    '112': string;
    '121': string;
    '128': string;
    '240': string;
    '258': string;
 *   };
 *   radii: {

 *   };
 *   shadows: {
    sm: string;
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
    "primary": "#290d00",
    "secondary": "#b36b13",
    "accent": "#d2c4a9",
    "background": "#010304",
    "foreground": "#000000",
    "neutral50": "#e5e7eb",
    "neutral100": "#050302",
    "neutral200": "#6c6557",
    "neutral300": "#b2a285"
  },
  "fonts": {
    "body": "'Bodoni Moda', sans-serif"
  },
  "fontSizes": {
    "16": "16px",
    "18": "18px",
    "19": "19px",
    "21": "21px",
    "23": "23px",
    "64": "64px",
    "101.12": "101.12px",
    "81.92": "81.92px",
    "44.8": "44.8px",
    "39.04": "39.04px",
    "24.32": "24.32px",
    "15.5": "15.5px"
  },
  "space": {
    "2": "2px",
    "56": "56px",
    "64": "64px",
    "80": "80px",
    "96": "96px",
    "112": "112px",
    "121": "121px",
    "128": "128px",
    "240": "240px",
    "258": "258px"
  },
  "radii": {},
  "shadows": {
    "sm": "oklab(0.42 0.0327558 0.100812 / 0.45) 0px 0px 0px 1px"
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
      "main": "#290d00",
      "light": "hsl(19, 100%, 23%)",
      "dark": "hsl(19, 100%, 10%)"
    },
    "secondary": {
      "main": "#b36b13",
      "light": "hsl(33, 81%, 54%)",
      "dark": "hsl(33, 81%, 24%)"
    },
    "background": {
      "default": "#010304",
      "paper": "#000102"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#d5cbb8"
    }
  },
  "typography": {
    "fontFamily": "'Newsreader', sans-serif",
    "h1": {
      "fontSize": "39.04px",
      "fontWeight": "500",
      "lineHeight": "41.3824px"
    },
    "h2": {
      "fontSize": "24.32px",
      "fontWeight": "500",
      "lineHeight": "28.2112px"
    }
  },
  "shape": {},
  "shadows": [
    "oklab(0.772 0.0129615 0.123321 / 0.42) 0px 0px 0px 1px",
    "oklab(0.42 0.0327558 0.100812 / 0.45) 0px 0px 0px 1px"
  ]
};

export default theme;
