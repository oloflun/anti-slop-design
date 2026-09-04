// React Theme — extracted from https://paya.ar
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
 *   };
 *   fonts: {
    body: string;
 *   };
 *   fontSizes: {
    '11': string;
    '14': string;
    '16': string;
    '18': string;
 *   };
 *   space: {
    '2': string;
    '192': string;
    '272': string;
    '483': string;
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
    "primary": "#eaff62",
    "secondary": "#377648",
    "background": "#377648",
    "foreground": "#000000",
    "neutral50": "#000000"
  },
  "fonts": {
    "body": "'Tuppence', sans-serif"
  },
  "fontSizes": {
    "11": "11px",
    "14": "14px",
    "16": "16px",
    "18": "18px"
  },
  "space": {
    "2": "2px",
    "192": "192px",
    "272": "272px",
    "483": "483px"
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
      "main": "#eaff62",
      "light": "hsl(68, 100%, 84%)",
      "dark": "hsl(68, 100%, 54%)"
    },
    "secondary": {
      "main": "#377648",
      "light": "hsl(136, 36%, 49%)",
      "dark": "hsl(136, 36%, 19%)"
    },
    "background": {
      "default": "#377648",
      "paper": "#377648"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#eaff62"
    }
  },
  "typography": {
    "fontFamily": "'Times New Roman', sans-serif",
    "body1": {
      "fontSize": "16px",
      "fontWeight": "400",
      "lineHeight": "16px"
    },
    "body2": {
      "fontSize": "11px",
      "fontWeight": "400",
      "lineHeight": "11px"
    }
  },
  "shape": {},
  "shadows": []
};

export default theme;
