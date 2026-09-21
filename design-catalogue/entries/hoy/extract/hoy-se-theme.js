// React Theme — extracted from https://www.hoy.se/
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
 *   };
 *   fonts: {
    body: string;
 *   };
 *   fontSizes: {
    '14': string;
    '16': string;
    '22': string;
    '32': string;
    '48': string;
    '88': string;
    '132': string;
 *   };
 *   space: {
    '0': string;
    '64': string;
    '96': string;
    '120': string;
    '160': string;
    '192': string;
 *   };
 *   radii: {
    xs: string;
    full: string;
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
    "primary": "#fcecba",
    "secondary": "#5124ae",
    "background": "#5124ae",
    "foreground": "#000000",
    "neutral50": "#e5e7eb",
    "neutral100": "#000000"
  },
  "fonts": {
    "body": "'Times New Roman', sans-serif"
  },
  "fontSizes": {
    "14": "14px",
    "16": "16px",
    "22": "22px",
    "32": "32px",
    "48": "48px",
    "88": "88px",
    "132": "132px"
  },
  "space": {
    "0": "0px",
    "64": "64px",
    "96": "96px",
    "120": "120px",
    "160": "160px",
    "192": "192px"
  },
  "radii": {
    "xs": "2px",
    "full": "9999px"
  },
  "shadows": {
    "sm": "rgb(255, 255, 255) 0px 0px 0px 0px, rgba(59, 130, 246, 0.5) 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 10px 15px -3px, rgba(0, 0, 0, 0.1) 0px 4px 6px -4px"
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
      "main": "#fcecba",
      "light": "hsl(45, 92%, 95%)",
      "dark": "hsl(45, 92%, 71%)"
    },
    "secondary": {
      "main": "#5124ae",
      "light": "hsl(260, 66%, 56%)",
      "dark": "hsl(260, 66%, 26%)"
    },
    "background": {
      "default": "#5124ae",
      "paper": "#fcecba"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#fcecba"
    }
  },
  "typography": {
    "fontFamily": "'Times New Roman', sans-serif",
    "h1": {
      "fontSize": "32px",
      "fontWeight": "400",
      "lineHeight": "44.8px"
    },
    "h3": {
      "fontSize": "22px",
      "fontWeight": "400",
      "lineHeight": "30.8px"
    },
    "body1": {
      "fontSize": "16px",
      "fontWeight": "400",
      "lineHeight": "24px"
    }
  },
  "shape": {
    "borderRadius": 2
  },
  "shadows": [
    "rgb(255, 255, 255) 0px 0px 0px 0px, rgba(59, 130, 246, 0.5) 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 10px 15px -3px, rgba(0, 0, 0, 0.1) 0px 4px 6px -4px"
  ]
};

export default theme;
