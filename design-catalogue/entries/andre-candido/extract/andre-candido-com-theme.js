// React Theme — extracted from https://www.andre-candido.com/
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
    neutral600: string;
 *   };
 *   fonts: {
    body: string;
    heading: string;
 *   };
 *   fontSizes: {
    '12': string;
    '14': string;
    '15': string;
    '16': string;
    '18': string;
    '24': string;
    '40': string;
    '48': string;
    '72': string;
    '160': string;
    '70.4': string;
    '12.8': string;
 *   };
 *   space: {
    '3': string;
    '30': string;
    '40': string;
    '60': string;
    '80': string;
    '112': string;
    '140': string;
    '170': string;
 *   };
 *   radii: {
    md: string;
    xl: string;
    full: string;
 *   };
 *   shadows: {
    xs: string;
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
    "primary": "#111118",
    "secondary": "#0000ee",
    "accent": "#fef199",
    "background": "#ffffff",
    "foreground": "#000000",
    "neutral50": "#ffffff",
    "neutral100": "#000000",
    "neutral200": "#222222",
    "neutral300": "#333333",
    "neutral400": "#7c7c7c",
    "neutral500": "#445567",
    "neutral600": "#dddddd"
  },
  "fonts": {
    "body": "'webflow-icons', sans-serif",
    "heading": "'Editorial New', sans-serif"
  },
  "fontSizes": {
    "12": "12px",
    "14": "14px",
    "15": "15px",
    "16": "16px",
    "18": "18px",
    "24": "24px",
    "40": "40px",
    "48": "48px",
    "72": "72px",
    "160": "160px",
    "70.4": "70.4px",
    "12.8": "12.8px"
  },
  "space": {
    "3": "3px",
    "30": "30px",
    "40": "40px",
    "60": "60px",
    "80": "80px",
    "112": "112px",
    "140": "140px",
    "170": "170px"
  },
  "radii": {
    "md": "8px",
    "xl": "24px",
    "full": "800px"
  },
  "shadows": {
    "xs": "rgba(51, 51, 51, 0.4) 0px 0px 3px 0px"
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
      "main": "#111118",
      "light": "hsl(240, 17%, 23%)",
      "dark": "hsl(240, 17%, 10%)"
    },
    "secondary": {
      "main": "#0000ee",
      "light": "hsl(240, 100%, 62%)",
      "dark": "hsl(240, 100%, 32%)"
    },
    "background": {
      "default": "#ffffff",
      "paper": "#dddddd"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#111118"
    }
  },
  "typography": {
    "fontFamily": "'webflow-icons', sans-serif",
    "h1": {
      "fontSize": "40px",
      "fontWeight": "400",
      "lineHeight": "48px",
      "fontFamily": "'Editorial New', sans-serif"
    },
    "h2": {
      "fontSize": "24px",
      "fontWeight": "400",
      "lineHeight": "28.8px",
      "fontFamily": "'Editorial New', sans-serif"
    }
  },
  "shape": {
    "borderRadius": 8
  },
  "shadows": [
    "rgba(51, 51, 51, 0.4) 0px 0px 3px 0px"
  ]
};

export default theme;
