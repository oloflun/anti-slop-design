// React Theme — extracted from https://dovetail.no/
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
    neutral300: string;
 *   };
 *   fonts: {
    body: string;
 *   };
 *   fontSizes: {
    '16': string;
    '20': string;
    '22': string;
    '28': string;
    '32': string;
    '48': string;
    '72': string;
 *   };
 *   space: {
    '3': string;
    '40': string;
    '56': string;
    '65': string;
    '72': string;
    '80': string;
    '90': string;
    '112': string;
    '127': string;
    '160': string;
    '310': string;
    '374': string;
 *   };
 *   radii: {
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
    "primary": "#f9e5b1",
    "secondary": "#ede5dc",
    "background": "#f9e5b1",
    "foreground": "#000000",
    "neutral50": "#e5e7eb",
    "neutral100": "#1d1e21",
    "neutral200": "#000000",
    "neutral300": "#fef9f3"
  },
  "fonts": {
    "body": "'Lausanne', sans-serif"
  },
  "fontSizes": {
    "16": "16px",
    "20": "20px",
    "22": "22px",
    "28": "28px",
    "32": "32px",
    "48": "48px",
    "72": "72px"
  },
  "space": {
    "3": "3px",
    "40": "40px",
    "56": "56px",
    "65": "65px",
    "72": "72px",
    "80": "80px",
    "90": "90px",
    "112": "112px",
    "127": "127px",
    "160": "160px",
    "310": "310px",
    "374": "374px"
  },
  "radii": {
    "lg": "16px",
    "xl": "24px",
    "full": "9999px"
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
      "main": "#f9e5b1",
      "light": "hsl(43, 86%, 95%)",
      "dark": "hsl(43, 86%, 69%)"
    },
    "secondary": {
      "main": "#ede5dc",
      "light": "hsl(32, 32%, 95%)",
      "dark": "hsl(32, 32%, 75%)"
    },
    "background": {
      "default": "#f9e5b1",
      "paper": "#dfe4f3"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#1d1e21"
    }
  },
  "typography": {
    "h1": {
      "fontSize": "32px",
      "fontWeight": "400",
      "lineHeight": "48px"
    },
    "h2": {
      "fontSize": "28px",
      "fontWeight": "600",
      "lineHeight": "28px"
    },
    "h3": {
      "fontSize": "20px",
      "fontWeight": "400",
      "lineHeight": "28px"
    }
  },
  "shape": {
    "borderRadius": 16
  },
  "shadows": []
};

export default theme;
