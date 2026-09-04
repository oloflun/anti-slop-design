// React Theme — extracted from https://www.caractere-bois.fr
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
    '16': string;
    '40': string;
    '100': string;
    '136': string;
    '51.2': string;
 *   };
 *   space: {
    '2': string;
    '40': string;
    '48': string;
    '58': string;
    '82': string;
    '370': string;
    '478': string;
 *   };
 *   radii: {
    md: string;
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
    "primary": "#f4300f",
    "secondary": "#0000ee",
    "accent": "#9cc4ff",
    "background": "#ffffff",
    "foreground": "#000000",
    "neutral50": "#333333",
    "neutral100": "#eaeaea",
    "neutral200": "#000000",
    "neutral300": "#ffffff"
  },
  "fonts": {
    "body": "'PP migra', sans-serif"
  },
  "fontSizes": {
    "14": "14px",
    "16": "16px",
    "40": "40px",
    "100": "100px",
    "136": "136px",
    "51.2": "51.2px"
  },
  "space": {
    "2": "2px",
    "40": "40px",
    "48": "48px",
    "58": "58px",
    "82": "82px",
    "370": "370px",
    "478": "478px"
  },
  "radii": {
    "md": "8px"
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
      "main": "#f4300f",
      "light": "hsl(9, 91%, 66%)",
      "dark": "hsl(9, 91%, 36%)"
    },
    "secondary": {
      "main": "#0000ee",
      "light": "hsl(240, 100%, 62%)",
      "dark": "hsl(240, 100%, 32%)"
    },
    "background": {
      "default": "#ffffff",
      "paper": "#eaeaea"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#333333"
    }
  },
  "typography": {
    "fontFamily": "'PP migra', sans-serif",
    "h1": {
      "fontSize": "40px",
      "fontWeight": "400",
      "lineHeight": "40px"
    },
    "body1": {
      "fontSize": "16px",
      "fontWeight": "400",
      "lineHeight": "normal"
    },
    "body2": {
      "fontSize": "14px",
      "fontWeight": "400",
      "lineHeight": "20px"
    }
  },
  "shape": {
    "borderRadius": 8
  },
  "shadows": []
};

export default theme;
