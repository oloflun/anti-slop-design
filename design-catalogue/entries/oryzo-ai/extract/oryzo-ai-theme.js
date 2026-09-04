// React Theme — extracted from https://oryzo.ai
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
    mono: string;
 *   };
 *   fontSizes: {
    '192': string;
    '364': string;
    '201.481': string;
    '130.37': string;
    '109.333': string;
    '57.1437': string;
    '45.3333': string;
    '43.7333': string;
    '42.88': string;
    '38.6735': string;
    '36.2667': string;
    '32.5178': string;
 *   };
 *   space: {
    '1': string;
    '27': string;
    '36': string;
    '40': string;
    '43': string;
    '48': string;
    '56': string;
    '60': string;
    '64': string;
    '69': string;
    '76': string;
    '96': string;
    '107': string;
    '181': string;
    '280': string;
    '364': string;
 *   };
 *   radii: {
    lg: string;
    xl: string;
    full: string;
 *   };
 *   shadows: {
    xs: string;
    sm: string;
    md: string;
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
    "primary": "#382416",
    "secondary": "#ffedd7",
    "accent": "#dc5000",
    "background": "#100904",
    "foreground": "#ffedd7",
    "neutral50": "#100904",
    "neutral100": "#445231",
    "neutral200": "#bbac97",
    "neutral300": "#6c5f51",
    "neutral400": "#000000",
    "neutral500": "#5d6c49",
    "neutral600": "#201914"
  },
  "fonts": {
    "body": "'Literata', sans-serif",
    "mono": "'DM Mono', monospace"
  },
  "fontSizes": {
    "192": "192px",
    "364": "364px",
    "201.481": "201.481px",
    "130.37": "130.37px",
    "109.333": "109.333px",
    "57.1437": "57.1437px",
    "45.3333": "45.3333px",
    "43.7333": "43.7333px",
    "42.88": "42.88px",
    "38.6735": "38.6735px",
    "36.2667": "36.2667px",
    "32.5178": "32.5178px"
  },
  "space": {
    "1": "1px",
    "27": "27px",
    "36": "36px",
    "40": "40px",
    "43": "43px",
    "48": "48px",
    "56": "56px",
    "60": "60px",
    "64": "64px",
    "69": "69px",
    "76": "76px",
    "96": "96px",
    "107": "107px",
    "181": "181px",
    "280": "280px",
    "364": "364px"
  },
  "radii": {
    "lg": "12px",
    "xl": "20px",
    "full": "100px"
  },
  "shadows": {
    "xs": "rgb(255, 160, 0) 0px 0px 3px 2px inset, rgb(224, 112, 16) 0px 0px 8px 4px inset",
    "sm": "rgba(255, 160, 0, 0.6) 0px 0px 5px 2px inset, rgb(224, 112, 16) 0px 0px 15px 8px inset, rgba(230, 100, 10, 0.45) 0px 0px 35px 15px inset, rgba(230, 80, 10, 0.35) 0px 0px 45px 20px inset",
    "md": "rgba(255, 140, 0, 0.6) 0px 0px 10px 3px, rgba(230, 80, 10, 0.25) 0px 0px 60px 45px"
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
      "main": "#382416",
      "light": "hsl(25, 44%, 30%)",
      "dark": "hsl(25, 44%, 10%)"
    },
    "secondary": {
      "main": "#ffedd7",
      "light": "hsl(33, 100%, 95%)",
      "dark": "hsl(33, 100%, 77%)"
    },
    "background": {
      "default": "#100904",
      "paper": "#445231"
    },
    "text": {
      "primary": "#ffedd7",
      "secondary": "#dc5000"
    }
  },
  "typography": {
    "fontFamily": "'Arial', sans-serif",
    "h1": {
      "fontSize": "57.1437px",
      "fontWeight": "600",
      "lineHeight": "68.5724px"
    }
  },
  "shape": {
    "borderRadius": 12
  },
  "shadows": [
    "rgb(255, 160, 0) 0px 0px 3px 2px inset, rgb(224, 112, 16) 0px 0px 8px 4px inset",
    "rgba(255, 160, 0, 0.6) 0px 0px 5px 2px inset, rgb(224, 112, 16) 0px 0px 15px 8px inset, rgba(230, 100, 10, 0.45) 0px 0px 35px 15px inset, rgba(230, 80, 10, 0.35) 0px 0px 45px 20px inset",
    "rgba(255, 140, 0, 0.6) 0px 0px 10px 3px",
    "rgba(255, 140, 0, 0.6) 0px 0px 10px 3px, rgba(230, 80, 10, 0.25) 0px 0px 60px 45px"
  ]
};

export default theme;
