// React Theme — extracted from https://apolloworkspace.com
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
    '12': string;
    '14': string;
    '16': string;
    '18': string;
    '24': string;
    '56': string;
    '72': string;
 *   };
 *   space: {
    '8': string;
    '64': string;
    '112': string;
    '207': string;
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
    "primary": "#e97451",
    "secondary": "#2d0f06",
    "accent": "#918037",
    "background": "#e1dccf",
    "foreground": "#3c261c",
    "neutral50": "#f9f8f0",
    "neutral100": "#0c0503",
    "neutral200": "#6f675e",
    "neutral300": "#e1dccf"
  },
  "fonts": {
    "body": "'paradigm-pro', sans-serif"
  },
  "fontSizes": {
    "12": "12px",
    "14": "14px",
    "16": "16px",
    "18": "18px",
    "24": "24px",
    "56": "56px",
    "72": "72px"
  },
  "space": {
    "8": "8px",
    "64": "64px",
    "112": "112px",
    "207": "207px"
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
      "main": "#e97451",
      "light": "hsl(14, 78%, 77%)",
      "dark": "hsl(14, 78%, 47%)"
    },
    "secondary": {
      "main": "#2d0f06",
      "light": "hsl(14, 76%, 25%)",
      "dark": "hsl(14, 76%, 10%)"
    },
    "background": {
      "default": "#e1dccf",
      "paper": "#0c0503"
    },
    "text": {
      "primary": "#3c261c",
      "secondary": "#e97451"
    }
  },
  "typography": {
    "h1": {
      "fontSize": "56px",
      "fontWeight": "300",
      "lineHeight": "58.8px"
    },
    "h2": {
      "fontSize": "24px",
      "fontWeight": "300",
      "lineHeight": "33px"
    },
    "body1": {
      "fontSize": "16px",
      "fontWeight": "400",
      "lineHeight": "24px"
    },
    "body2": {
      "fontSize": "14px",
      "fontWeight": "500",
      "lineHeight": "20px"
    }
  },
  "shape": {},
  "shadows": []
};

export default theme;
