// React Theme — extracted from https://vistal.webflow.io
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
    neutral700: string;
 *   };
 *   fonts: {
    body: string;
 *   };
 *   fontSizes: {
    '12': string;
    '14': string;
    '16': string;
    '24': string;
    '40': string;
    '48': string;
    '64': string;
    '72': string;
    '80': string;
 *   };
 *   space: {
    '2': string;
    '32': string;
    '40': string;
    '60': string;
    '72': string;
    '95': string;
    '109': string;
    '120': string;
    '240': string;
    '247': string;
    '298': string;
    '332': string;
 *   };
 *   radii: {
    xs: string;
    md: string;
    lg: string;
    xl: string;
    full: string;
 *   };
 *   shadows: {
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
    "primary": "#ebf213",
    "secondary": "#8f00ff",
    "accent": "#efd556",
    "background": "#ffffff",
    "foreground": "#000000",
    "neutral50": "#000000",
    "neutral100": "#ffffff",
    "neutral200": "#656565",
    "neutral300": "#131313",
    "neutral400": "#333333",
    "neutral500": "#f0efed",
    "neutral600": "#bababa",
    "neutral700": "#c8c8c8"
  },
  "fonts": {
    "body": "'webflow-icons', sans-serif"
  },
  "fontSizes": {
    "12": "12px",
    "14": "14px",
    "16": "16px",
    "24": "24px",
    "40": "40px",
    "48": "48px",
    "64": "64px",
    "72": "72px",
    "80": "80px"
  },
  "space": {
    "2": "2px",
    "32": "32px",
    "40": "40px",
    "60": "60px",
    "72": "72px",
    "95": "95px",
    "109": "109px",
    "120": "120px",
    "240": "240px",
    "247": "247px",
    "298": "298px",
    "332": "332px"
  },
  "radii": {
    "xs": "2px",
    "md": "8px",
    "lg": "12px",
    "xl": "24px",
    "full": "100px"
  },
  "shadows": {
    "xl": "rgba(0, 0, 0, 0.1) 0px 14px 32px 0px, rgba(0, 0, 0, 0.09) 0px 58px 58px 0px, rgba(0, 0, 0, 0.05) 0px 130px 78px 0px, rgba(0, 0, 0, 0.01) 0px 232px 93px 0px, rgba(0, 0, 0, 0) 0px 362px 101px 0px"
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
      "main": "#ebf213",
      "light": "hsl(62, 90%, 66%)",
      "dark": "hsl(62, 90%, 36%)"
    },
    "secondary": {
      "main": "#8f00ff",
      "light": "hsl(274, 100%, 65%)",
      "dark": "hsl(274, 100%, 35%)"
    },
    "background": {
      "default": "#ffffff",
      "paper": "#000000"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#ffffff"
    }
  },
  "typography": {
    "fontFamily": "'webflow-icons', sans-serif",
    "h1": {
      "fontSize": "40px",
      "fontWeight": "500",
      "lineHeight": "48px"
    },
    "h2": {
      "fontSize": "24px",
      "fontWeight": "400",
      "lineHeight": "36px"
    }
  },
  "shape": {
    "borderRadius": 8
  },
  "shadows": [
    "rgba(0, 0, 0, 0.1) 0px 14px 32px 0px, rgba(0, 0, 0, 0.09) 0px 58px 58px 0px, rgba(0, 0, 0, 0.05) 0px 130px 78px 0px, rgba(0, 0, 0, 0.01) 0px 232px 93px 0px, rgba(0, 0, 0, 0) 0px 362px 101px 0px"
  ]
};

export default theme;
