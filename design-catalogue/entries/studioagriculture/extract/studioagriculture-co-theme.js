// React Theme — extracted from https://studioagriculture.co
// Compatible with: Chakra UI, Stitches, Vanilla Extract, or any CSS-in-JS

/**
 * TypeScript type definition for this theme:
 *
 * interface Theme {
 *   colors: {
    primary: string;
    secondary: string;
    background: string;
    foreground: string;
    neutral50: string;
    neutral100: string;
    neutral200: string;
 *   };
 *   fonts: {
    body: string;
 *   };
 *   fontSizes: {
    '14': string;
    '16': string;
    '18': string;
    '38': string;
    '100': string;
 *   };
 *   space: {
    '5': string;
    '100': string;
    '165': string;
    '300': string;
 *   };
 *   radii: {

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
    "primary": "#e7371e",
    "secondary": "#671235",
    "background": "#ffffff",
    "foreground": "#000000",
    "neutral50": "#000000",
    "neutral100": "#ffffff",
    "neutral200": "#eeeeee"
  },
  "fonts": {
    "body": "'Macan', sans-serif"
  },
  "fontSizes": {
    "14": "14px",
    "16": "16px",
    "18": "18px",
    "38": "38px",
    "100": "100px"
  },
  "space": {
    "5": "5px",
    "100": "100px",
    "165": "165px",
    "300": "300px"
  },
  "radii": {},
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
      "main": "#e7371e",
      "light": "hsl(7, 81%, 66%)",
      "dark": "hsl(7, 81%, 36%)"
    },
    "secondary": {
      "main": "#671235",
      "light": "hsl(335, 70%, 39%)",
      "dark": "hsl(335, 70%, 10%)"
    },
    "background": {
      "default": "#ffffff",
      "paper": "#671235"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#ffffff"
    }
  },
  "typography": {
    "fontFamily": "'PP Neue Montreal', sans-serif",
    "h1": {
      "fontSize": "38px",
      "fontWeight": "400",
      "lineHeight": "41.8px"
    },
    "body1": {
      "fontSize": "16px",
      "fontWeight": "400",
      "lineHeight": "normal"
    },
    "body2": {
      "fontSize": "14px",
      "fontWeight": "400",
      "lineHeight": "normal"
    }
  },
  "shape": {},
  "shadows": []
};

export default theme;
